import java.util.*;

class Solution {

    List<Integer>[] graph;
    boolean[] visited;

    public int countCompleteComponents(int n, int[][] edges) {

        graph = new ArrayList[n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {

                int[] info = dfs(i);

                int nodes = info[0];
                int edgeCount = info[1] / 2;

                if (edgeCount == nodes * (nodes - 1) / 2)
                    ans++;
            }
        }

        return ans;
    }

    private int[] dfs(int node) {

        visited[node] = true;

        int nodes = 1;
        int edges = graph[node].size();

        for (int next : graph[node]) {
            if (!visited[next]) {
                int[] temp = dfs(next);
                nodes += temp[0];
                edges += temp[1];
            }
        }

        return new int[]{nodes, edges};
    }
}