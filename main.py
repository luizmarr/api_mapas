from services.mapas import Mapas
def main():
    mapas = Mapas()
    endereco = input("Digite um endereço: ")
    while not endereco.strip():
        print("Endereço não pode ser vazio.")
        endereco = input("Digite um endereço: ")
        
    resultado = mapas.geocode(endereco)

    if resultado:
        print(f"Endereço: {resultado['endereco']}")
        print(f"Latitude: {resultado['latitude']}")
        print(f"Longitude: {resultado['longitude']}")
        print(f"País: {resultado['pais']}")
    else:
        print("Endereço não encontrado.")
if __name__ == "__main__":    
    main()