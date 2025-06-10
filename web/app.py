from flask import Flask, render_template, jsonify
import sys
import os
import pandas as pd
from src.dataflow import DataFlow

app = Flask(__name__)

# Add the parent directory to Python path to import the DataFlow module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define the path to sales.csv
SALES_CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'examples', 'sales.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_pipeline/<int:pipeline_num>')
def execute_pipeline(pipeline_num):
    df = DataFlow()
    
    # Define the pipelines with the correct file path
    pipelines = {
        1: f"""
        carregar "{SALES_CSV_PATH}";
        ordenar por vendas desc;
        selecionar regiao, produto, vendas;
        mostrar tabela;
        """,
        2: f"""
        carregar "{SALES_CSV_PATH}";
        transformar valor_total = vendas * quantidade;
        agrupar por regiao;
        agregar soma de valor_total como total_regiao;
        ordenar por total_regiao desc;
        mostrar tabela;
        """,
        3: f"""
        carregar "{SALES_CSV_PATH}";
        filtrar vendas > 1000;
        transformar margem_lucro = vendas * 0.3;
        agrupar por produto;
        agregar media de margem_lucro como media_lucro;
        ordenar por media_lucro desc;
        selecionar produto, media_lucro;
        mostrar tabela;
        """
    }
    
    if pipeline_num not in pipelines:
        return jsonify({'error': 'Pipeline não encontrado'}), 404
    
    try:
        # Execute the pipeline
        result = df.executar(pipelines[pipeline_num])
        
        # Convert the result to HTML table
        if isinstance(result, pd.DataFrame):
            html_table = result.to_html(classes='table table-striped', index=False)
            return jsonify({
                'success': True,
                'html': html_table,
                'title': f'Resultado do Pipeline {pipeline_num}'
            })
        else:
            return jsonify({
                'success': True,
                'html': str(result),
                'title': f'Resultado do Pipeline {pipeline_num}'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 