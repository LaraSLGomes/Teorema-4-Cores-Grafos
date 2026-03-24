from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Representação do Grafo (Adjacências)
adjacencias = {
    'AC': ['AM', 'RO'], 'AL': ['BA', 'PE', 'SE'], 'AM': ['AC', 'MT', 'PA', 'RO', 'RR'],
    'AP': ['PA'], 'BA': ['AL', 'ES', 'GO', 'MG', 'PE', 'PI', 'SE', 'TO'],
    'CE': ['PB', 'PE', 'PI', 'RN'], 'DF': ['GO', 'MG'], 'ES': ['BA', 'MG', 'RJ'],
    'GO': ['BA', 'DF', 'MG', 'MS', 'MT', 'TO'], 'MA': ['PA', 'PI', 'TO'],
    'MG': ['BA', 'DF', 'ES', 'GO', 'MS', 'RJ', 'SP'], 'MS': ['GO', 'MG', 'MT', 'PR', 'SP'],
    'MT': ['AM', 'GO', 'MS', 'PA', 'RO', 'TO'], 'PA': ['AM', 'AP', 'MA', 'MT', 'RR', 'TO'],
    'PB': ['CE', 'PE', 'RN'], 'PE': ['AL', 'BA', 'CE', 'PB', 'PI'],
    'PI': ['BA', 'CE', 'MA', 'PE', 'TO'], 'PR': ['MS', 'SC', 'SP'],
    'RJ': ['ES', 'MG', 'SP'], 'RN': ['CE', 'PB'], 'RO': ['AC', 'AM', 'MT'],
    'RR': ['AM', 'PA'], 'RS': ['SC'], 'SC': ['PR', 'RS'], 'SE': ['AL', 'BA'],
    'SP': ['MG', 'MS', 'PR', 'RJ'], 'TO': ['BA', 'GO', 'MA', 'MT', 'PA', 'PI']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/executar_algoritmo')
def executar():
    # Cores 
    paleta = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']
    coloracao = {}
    
    # HEURÍSTICA: Ordenar estados pelo número de vizinhos (Grau do Vértice)
    # Estados com mais vizinhos são coloridos primeiro para evitar conflitos
    ordem_processamento = sorted(adjacencias.keys(), key=lambda x: len(adjacencias[x]), reverse=True)

    for estado in ordem_processamento:
        # Descobre cores dos vizinhos já processados
        cores_ocupadas = [coloracao[v] for v in adjacencias[estado] if v in coloracao]
        
        # ALGORITMO GULOSO: Pega a primeira cor que não está nos vizinhos
        for cor in paleta:
            if cor not in cores_ocupadas:
                coloracao[estado] = cor
                break
                
    return jsonify(coloracao)

if __name__ == '__main__':
    app.run(debug=True)