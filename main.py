import os

TOKEN = os.getenv("TOKEN")

import discord
from discord.ext import commands
from config import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

BANNER_URL = BANNER if "BANNER" in globals() else "https://i.imgur.com/placeholder.png"


# ============================
# CHECKOUT (PIX)
# ============================
class CheckoutView(discord.ui.View):
    def __init__(self, produto, dados):
        super().__init__(timeout=None)
        self.produto = produto
        self.dados = dados

    def gerar_pix(self, chave, valor):
        return f"{chave}|{valor:.2f}"

    @discord.ui.button(label="🔑 PIX Chave", style=discord.ButtonStyle.success)
    async def pix(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message(
            f"🔑 **PIX:** `{PIX_CHAVE}`\n📌 segure para copiar",
            ephemeral=True
        )

    @discord.ui.button(label="📋 PIX Copia e Cola", style=discord.ButtonStyle.secondary)
    async def copia(self, interaction: discord.Interaction, button: discord.ui.Button):

        valor = self.dados.get("preco", 0)
        pix = self.gerar_pix(PIX_CHAVE, valor)

        await interaction.response.send_message(
            f"💰 R$ {valor:.2f}\n\n```{pix}```",
            ephemeral=True
        )


# ============================
# TICKET
# ============================
class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📋 Info", style=discord.ButtonStyle.secondary)
    async def info(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "📦 Status: aguardando pagamento",
            ephemeral=True
        )

    @discord.ui.button(label="❌ Fechar Ticket", style=discord.ButtonStyle.danger)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🔒 fechando...", ephemeral=True)
        await interaction.channel.delete()


# ============================
# PRODUTO
# ============================
def create_product_embed(produto, dados):
    embed = discord.Embed(
        title=f"🛒 {produto}",
        description="💎 Loja digital\n💳 PIX disponível",
        color=COR or 0x7C4DFF
    )

    embed.add_field(name="💰 Preço", value=f"R$ {dados.get('preco', 0):.2f}", inline=True)
    embed.add_field(name="📦 Estoque", value=dados.get("estoque", 0), inline=True)
    embed.add_field(name="📄 Descrição", value=dados.get("descricao", "Sem descrição"), inline=False)

    embed.set_image(url=BANNER_URL)
    return embed


# ============================
# PRODUCT VIEW
# ============================
class ProductView(discord.ui.View):
    def __init__(self, produto, dados):
        super().__init__(timeout=None)
        self.produto = produto
        self.dados = dados

    @discord.ui.button(label="Comprar", style=discord.ButtonStyle.success)
    async def buy(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        categoria = discord.utils.get(guild.categories, name=CATEGORIA_PEDIDOS)

        canal = await guild.create_text_channel(
            name=f"pedido-{interaction.user.id}",
            category=categoria
        )

        await canal.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await canal.set_permissions(guild.default_role, view_channel=False)

        embed = discord.Embed(
            title="🧾 Checkout iniciado",
            description="Envie o comprovante do PIX aqui",
            color=COR or 0x7C4DFF
        )

        embed.add_field(name="Produto", value=self.produto, inline=False)
        embed.add_field(name="Preço", value=f"R$ {self.dados.get('preco', 0):.2f}", inline=True)

        embed.set_image(url=BANNER_URL)

        await canal.send(embed=embed)
        await canal.send("📌 envie comprovante do pix")
        await canal.send(view=TicketView())
        await canal.send(view=CheckoutView(self.produto, self.dados))

        await interaction.response.send_message(
            f"Pedido criado: {canal.mention}",
            ephemeral=True
        )


# ============================
# LOJA
# ============================
class LojaView(discord.ui.View):
    def __init__(self):
        super().__init__()

        for produto, dados in (PRODUTOS or {}).items():
            self.add_item(self.make_button(produto, dados))

    def make_button(self, produto, dados):

        async def callback(interaction: discord.Interaction):
            embed = create_product_embed(produto, dados)
            view = ProductView(produto, dados)

            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        btn = discord.ui.Button(
            label=produto,
            style=discord.ButtonStyle.secondary,
            emoji="🛒"
        )

        btn.callback = callback
        return btn


# ============================
# PAINEL
# ============================
@bot.tree.command(name="painel", description="Loja")
async def painel(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🏪 MARKETPLACE APP",
        description=(
            "━━━━━━━━━━━━━━━━━━\n"
            "💎 Loja oficial de produtos digitais\n"
            "💳 Pagamento via PIX\n"
            "⚡ Entrega automática/manual\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "👉 Escolha um produto abaixo para ver os detalhes."
        ),
        color=COR or 0x7C4DFF
    )

    embed.set_image(url=BANNER_URL)
    embed.set_footer(text="App Store • Discord Marketplace")

    await interaction.response.send_message(embed=embed, view=LojaView())


# ============================
# ESCOLA
# ============================
class EscolaView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="📚 Aula", style=discord.ButtonStyle.primary)
    async def aula(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("📚 Aula aberta", ephemeral=True)

    @discord.ui.button(label="📊 Notas", style=discord.ButtonStyle.secondary)
    async def notas(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("📊 sem notas", ephemeral=True)


@bot.tree.command(name="escola", description="Sistema escola")
async def escola(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🏫 ESCOLA",
        description="Sistema escolar",
        color=0x3498DB
    )

    await interaction.response.send_message(embed=embed, view=EscolaView())


# ============================
# START
# ============================
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot online: {bot.user}")


bot.run(TOKEN)
