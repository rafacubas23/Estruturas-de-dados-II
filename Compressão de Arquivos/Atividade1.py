def compactarLZW(textoOriginal):
    tamanhoDicionario = 256
    dicionario = {chr(i): i for i in range(tamanhoDicionario)}

    palavraAtual = ""
    resultadoCompactado = []

    for caractere in textoOriginal:
        novaPalavra = palavraAtual + caractere
        if novaPalavra in dicionario:
            palavraAtual = novaPalavra
        else:
            resultadoCompactado.append(dicionario[palavraAtual])
            dicionario[novaPalavra] = tamanhoDicionario
            tamanhoDicionario += 1
            palavraAtual = caractere

    if palavraAtual:
        resultadoCompactado.append(dicionario[palavraAtual])

    return resultadoCompactado

def descompactarLZW(listaCompactada):
    tamanhoDicionario = 256
    dicionario = {i: chr(i) for i in range(tamanhoDicionario)}

    resultadoDescompactado = []

    codigoAnterior = listaCompactada.pop(0)
    palavraAnterior = dicionario[codigoAnterior]
    resultadoDescompactado.append(palavraAnterior)

    for codigoAtual in listaCompactada:
        if codigoAtual in dicionario:
            entrada = dicionario[codigoAtual]
        elif codigoAtual == tamanhoDicionario:
            entrada = palavraAnterior + palavraAnterior[0]
        else:
            raise ValueError("Código inválido durante a descompactação.")

        resultadoDescompactado.append(entrada)
        dicionario[tamanhoDicionario] = palavraAnterior + entrada[0]
        tamanhoDicionario += 1
        palavraAnterior = entrada

    return ''.join(resultadoDescompactado)

if __name__ == "__main__":
    texto = "ABCABCABC"
    print("Texto original:", texto)

    textoCompactado = compactarLZW(texto)
    print("Compactado:", textoCompactado)

    textoDescompactado = descompactarLZW(textoCompactado.copy())
    print("Descompactado:", textoDescompactado)
