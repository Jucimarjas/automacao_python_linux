import subprocess as sp

def install_essential_packages():
    packages = ["vim", "curl", "wget", "htop", "git"]

    for package in packages:
        print(f"Instalando {package}...")
        sp.run(["sudo", "apt", "install", "-y", package])

    print("Pacotes essenciais instalados com sucesso")
    
install_essential_packages()