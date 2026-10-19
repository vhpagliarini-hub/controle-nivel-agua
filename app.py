
try:
    from colorama import Fore, Style, init
except ImportError:
    class _ColorFallback:
        RED = ""
        YELLOW = ""
        GREEN = ""
        CYAN = ""
        BLUE = ""
        RESET = ""

    class Fore:
        RED = ""
        YELLOW = ""
        GREEN = ""
        CYAN = ""
        BLUE = ""

    class Style:
        RESET_ALL = ""

    def init(*args, **kwargs):
        return None

init(autoreset=True)

niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

def definir_cor(nivel):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]

    return cores[nivel - 1]

for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)
