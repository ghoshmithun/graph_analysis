import pickle
import numpy as np
import math
import matplotlib.pyplot as plt

BIG_PICKLE_DEGREE = '../degree_file_from_adjacency_big.pickle'
BIG_GRAPH_POWER_GRAPH = '../analysis/power_law_plot_big.png'
BIG_GRAPH_TEXT = r'Degree dist from Big Orkut Graph alpha = {:.3f}'

SMALL_PICKLE_DEGREE = '../degree_file_from_adjlist_small.pickle'
SMALL_GRAPH_POWER_GRAPH = '../analysis/power_law_plot_small.png'
SMALL_GRAPH_TEXT = r'Degree dist from Small Web UK Graph alpha = {:.3f}'


def plot_power_graph(pickle_degrees,file_to_save,text):
    with open(pickle_degrees,"rb") as f:
        degee_dist=pickle.load(f)
        degee_dist = {k:v for (k,v) in sorted(degee_dist.items(),key=lambda x: x[1],reverse=True)}
        num_nodes=list(degee_dist.keys())
        total_nodes=sum(num_nodes)
        prob_nodes = list(map(lambda x: (x/total_nodes),num_nodes))
        log_prob_nodes = list(map(math.log,prob_nodes))
        degrees = list(degee_dist.values())
        log_degrees = list(map(math.log,degrees))
        a = np.corrcoef(log_prob_nodes, log_degrees)[0][1]
        z = np.polyfit(log_prob_nodes, log_degrees,1)
        #Power law is probability that a node has k neighbours is P(k) ~ k ^(-a) lnP(k) ~ -a*lnk
        plt.subplot(2, 1, 1)
        plt.plot(num_nodes, degrees, 'kx')
        plt.xscale('log')
        plt.yscale('log')
        plt.title(text.format(a))
        plt.subplot(2, 1, 2)
        p = np.poly1d(z)
        xp = np.linspace(min(log_prob_nodes)-0.5,max(log_prob_nodes)+0.5,100)
        plt.plot(log_prob_nodes, log_degrees, '.', xp, p(xp), '--')
        plt.title("Log Probability Nodes and Log Degrees Line Fit")
        plt.savefig(file_to_save)


if __name__ == '__main__':
    plot_power_graph(BIG_PICKLE_DEGREE,BIG_GRAPH_POWER_GRAPH,BIG_GRAPH_TEXT)
    plot_power_graph(SMALL_PICKLE_DEGREE, SMALL_GRAPH_POWER_GRAPH, SMALL_GRAPH_TEXT)



