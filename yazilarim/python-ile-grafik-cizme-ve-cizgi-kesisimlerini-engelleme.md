# 📉 Python ile grafik çizme ve çizgi kesişimlerini engelleme

## Python ile grafik çizme ve çizgi kesişimlerini engelleme

<img src="../.gitbook/assets/image (121).png" alt="" data-size="original">

* `circular_layout` ile çizgilerin çakışmasını engelliyoruz

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Core emotions
joy = "Sevinç"
trust = "Güven"
fear = "Korku"
surprise = "Şaşkınlık"
sadness = "Üzüntü"
disgust = "İğrenme"
anger = "Öfke"
anticipation = "Beklenti"

# Emotions that are generated from core emotions
optimism = "Optimizm"  # joy + anticipation
guilt = "Suçluluk"  # joy + fear
pleasure = "Haz"  # joy + surprise
ailment = "Marazlık"  # joy + disgust
arrogance = "Kibir"  # joy + anger
love = "Aşk"  # joy + trust

fussiness = "Telaşlılık"  # anticipation + fear
cynicism = "Kinizm"  # anticipation + disgust
irriability = "Sinirlilik"  # anticipation + anger
jealousy = "Kıskançlık"  # anticipation + sadness
hope = "Umut"  # anticipation + trust

awe = "Haşmet"  # fear + surprise
despair = "Umutsuzluk"  # fear + sadness
shame = "Utanç"  # fear + disgust
submission = "Teslimiyet"  # fear + trust

disbelief = "İnanamama"  # surprise + disgust
rage = "Hiddet"  # surprise + anger
curiosity = "Merak"  # surprise + trust
disapproval = "Onaylamama"  # surprise + sadness

regret = "Pişmanlık"  # sadness + disgust
humiliate = "Aşağılamak"  # sadness + anger
sensibility = "İçlilik"  # sadness + trust

dominance = "Baskınlık"  # anger + trust

# Add the nodes 1, 2, and 3 to the graph
G.add_nodes_from([joy, trust, fear, surprise, sadness, disgust, anger, anticipation])

# Add an edge labeled "three" connecting all three nodes
G.add_edge(joy, anticipation, label=optimism)
G.add_edge(joy, fear, label=guilt)
G.add_edge(joy, surprise, label=pleasure)
G.add_edge(joy, disgust, label=ailment)
G.add_edge(joy, anger, label=arrogance)
G.add_edge(joy, trust, label=love)

G.add_edge(anticipation, fear, label=fussiness)
G.add_edge(anticipation, anger, label=rage)
G.add_edge(anticipation, sadness, label=jealousy)
G.add_edge(anticipation, trust, label=hope)

G.add_edge(fear, surprise, label=awe)
G.add_edge(fear, sadness, label=despair)
G.add_edge(fear, disgust, label=shame)
G.add_edge(fear, trust, label=submission)

G.add_edge(surprise, disgust, label=disbelief)
G.add_edge(surprise, anger, label=rage)
G.add_edge(surprise, trust, label=curiosity)
G.add_edge(surprise, sadness, label=disapproval)

G.add_edge(sadness, disgust, label=regret)
G.add_edge(sadness, anger, label=humiliate)
G.add_edge(sadness, trust, label=sensibility)

G.add_edge(anger, trust, label=dominance)

fig = plt.figure(figsize=(20, 12))

# Draw the graph
pos = nx.circular_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=3000)
nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, alpha=0.5, edge_color="b")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=nx.get_edge_attributes(G, "label"),
    font_size=12,
    font_family="sans-serif",
)

# Display the graph
plt.axis("off")
plt.show()
```

ChatGPT
