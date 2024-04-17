import java.io.*;
import java.util.*;

public class Main {    
    static boolean[] dfsVisited;
    static ArrayList<Integer> dfsQ = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken()) - 1;
        boolean[][] graph = new boolean[N][N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken()) - 1;
            int dst = Integer.parseInt(st.nextToken()) - 1;

            graph[src][dst] = true;
            graph[dst][src]= true;


        }
        StringBuilder sb = new StringBuilder();

        dfsVisited = new boolean[N];
        dfs(graph, V);
        for (int i = 0; i < dfsQ.size() - 1; i++) {
            sb.append(dfsQ.get(i) + 1);
            sb.append(" ");
        }
        sb.append(dfsQ.get(dfsQ.size() - 1) + 1);
        sb.append("\n");

        ArrayList<Integer> bfsQ = bfs(graph, V);
        for (int i = 0; i < bfsQ.size() - 1; i++) {
            sb.append(bfsQ.get(i) + 1);
            sb.append(" ");
        }
        sb.append(bfsQ.get(bfsQ.size() - 1) + 1);
        sb.append("\n");
        System.out.print(sb.toString());
    }

    static ArrayList<Integer> bfs(boolean[][] graph, int V) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] isVisited = new boolean[graph.length];

        ArrayList<Integer> visitedQ = new ArrayList<>();
        q.add(V);
        while (!q.isEmpty()) {
            int nextNode = q.remove();
            if (isVisited[nextNode]) continue;
            else {
                visitedQ.add(nextNode);
                isVisited[nextNode] = true;
                for (int i = 0; i < graph.length; i++) {
                    if (graph[nextNode][i]) q.add(i);
                }
            }
        }
        return visitedQ;
    }


    static void dfs(boolean[][] graph, int V) {
        if (dfsVisited[V]) return;
        dfsVisited[V] = true;
        dfsQ.add(V);
        for (int i = 0; i < graph.length; i++) {
            if (graph[V][i]) dfs(graph, i);
        }
    }
}