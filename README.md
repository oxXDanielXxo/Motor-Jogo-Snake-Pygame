# 🐍 Operação Serpente (Motor de Jogo 2D)

Um projeto de desenvolvimento de software focado em dominar a arquitetura fundamental de um "Game Loop". O projeto é um clone do clássico Snake (Jogo da Cobrinha), construído inteiramente do zero utilizando Python e a biblioteca gráfica Pygame.

## ⚙️ Tecnologias e Arquitetura
* **Linguagem:** Python
* **Motor Gráfico:** `pygame` para renderização 2D de interface, controle de frames por segundo (FPS) e escuta de eventos de hardware.

## 🚀 Funcionalidades de Engenharia Gráfica
* **Arquitetura de Game Loop:** Implementação do ciclo contínuo padrão da indústria: Captura de Inputs -> Atualização de Física -> Renderização de Tela.
* **State Management (Máquina de Estados):** Controle seguro entre os estados de "Partida Ativa" e "Game Over", utilizando retornos (`return`) e saídas limpas (`sys.exit()`) para evitar vazamentos de memória (memory leaks) durante a reinicialização de instâncias.
* **Sistema de Colisão em Grade:** O motor calcula ativamente a sobreposição de coordenadas cartesianas (X, Y) para detectar o consumo de alvos (crescimento da cobra) e colisões fatais (impacto contra as bordas da resolução ou intersecção com a matriz do próprio corpo).
* **Interface Resiliente (UI Fallback):** Sistema de renderização de fontes blindado contra falhas de sistema operacional, forçando o uso do pacote tipográfico padrão interno do Pygame.

## 💻 Como Executar
1. Clone este repositório.
2. Instale o motor gráfico: `pip install -r requirements.txt`
3. Dê a ignição no jogo: `python jogo.py`
4. Controles: Setas do teclado.
