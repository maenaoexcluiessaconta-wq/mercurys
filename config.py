# ============================
# CONFIGURAÇÃO DO BOT
# ============================

# ⚠️ No Render você NÃO precisa colocar TOKEN aqui
# Ele vem do Environment Variable (os.getenv)

COR = 0x7C4DFF

# Banner da loja
BANNER = "https://cdn.discordapp.com/attachments/1521006030241271998/1523405068819501126/IMG-20260705-WA0004.jpg?ex=6a4bfd07&is=6a4aab87&hm=155a7f5a5137d85308f47020be464d5274fe1d96beff63924d2375cc7023baa3&"

# Categoria onde os tickets serão criados
CATEGORIA_PEDIDOS = "🛒 PEDIDOS"

# Chave PIX (vai aparecer no checkout)
PIX_CHAVE = "44991796792"

# Produtos da loja
PRODUTOS = {
    "Produto Teste": {
        "preco": 10.00,
        "estoque": 5
    },
    "VIP Minecraft": {
        "preco": 25.00,
        "estoque": 10
    }
}
    "100 Lucky Spins + 100 Lucky Spins Ability": {
        "preco": 2.00,
        "estoque": 999,
        "descricao": "Pacote básico para começar com spins iniciais e ability spins."
    },

    "250 Lucky Spins + 250 Lucky Spins Ability": {
        "preco": 3.50,
        "estoque": 999,
        "descricao": "Pacote intermediário com mais chances de rolar spins e abilities."
    },

    "500 Lucky Spins + 500 Lucky Spins Ability": {
        "preco": 5.50,
        "estoque": 999,
        "descricao": "Bom custo-benefício para evoluir rápido com quantidade média de spins."
    },

    "1000 Lucky Spins + 1000 Lucky Spins Ability": {
        "preco": 12.50,
        "estoque": 999,
        "descricao": "Pacote avançado para quem quer progresso rápido e consistente."
    },

    "2500 Lucky Spins + 2500 Lucky Spins Ability": {
        "preco": 20.00,
        "estoque": 999,
        "descricao": "Pacote forte para evolução acelerada no jogo."
    },

    "5000 Lucky Spins + 5000 Lucky Spins Ability": {
        "preco": 35.00,
        "estoque": 999,
        "descricao": "Pacote premium com grande quantidade de spins para progresso máximo."
    }
}
