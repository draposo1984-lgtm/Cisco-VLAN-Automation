from flask import Flask, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = ""

    if request.method == "POST":

        try:
            ip = request.form["ip"]
            username = request.form["username"]
            password = request.form["password"]

            print(f"Conectando ao switch {ip}")

            hostname = request.form["hostname"]

            print("Conectado com sucesso!")

            print("CHEGUEI AQUI")

            vlan_id_1 = request.form["vlan_id_1"]
            vlan_nome_1 = request.form["vlan_nome_1"]

            vlan_id_2 = request.form["vlan_id_2"]
            vlan_nome_2 = request.form["vlan_nome_2"]

            vlan_id_3 = request.form["vlan_id_3"]
            vlan_nome_3 = request.form["vlan_nome_3"]

            switch = {
                "device_type": "cisco_ios",
                "host": ip,
                "username": username,
                "password": password
            }

            conn = ConnectHandler(**switch)

	    # Altera hostname primeiro

            conn.send_config_set([

            f"hostname {hostname}"
            ])

            # Atualiza o prompt após mudança

            conn.find_prompt()

            comandos = [
            f"vlan {vlan_id_1}",
            f"name {vlan_nome_1}",

            f"vlan {vlan_id_2}",
            f"name {vlan_nome_2}",

            f"vlan {vlan_id_3}",	
            f"name {vlan_nome_3}"
]

            resultado = conn.send_config_set(comandos)

            conn.save_config()

            from datetime import datetime

            backup = conn.send_command("show running-config")

            hostname_switch = conn.find_prompt().replace("#", "")

            data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

            nome_arquivo = f"backup/{hostname_switch}_{data_hora}.txt"

            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(backup)

            conn.disconnect()

            resultado = f""" 
       ✅ Configuração aplicada com sucesso!

       ✅ Configuração salva na NVRAM com sucesso!

       ✅ Backup realizado com sucesso!

  Arquivo gerado:
  {nome_arquivo}
 
  Hostname: {hostname}

  VLAN {vlan_id_1}: {vlan_nome_1}

  VLAN {vlan_id_2}: {vlan_nome_2}

  VLAN {vlan_id_3}: {vlan_nome_3}
  """
            
        except Exception as erro:
            resultado = f"ERRO: {erro}"

    return render_template(
        "index.html",
        resultado=resultado
    )

if __name__ == "__main__":
    app.run(debug=True)