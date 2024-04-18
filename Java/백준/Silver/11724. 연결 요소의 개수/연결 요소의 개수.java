import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        boolean[][] graph = new boolean[N][N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            graph[a][b] = true;
            graph[b][a] = true;
        }

        int unionCnt = 0;
        boolean[] visitied = new boolean[N];

        for (int i = 0; i < N; i++) {
            if (visitied[i]) continue;
            else {
                unionCnt += 1;
                Queue<Integer> q = new LinkedList<>();
                q.add(i);
                while (!q.isEmpty()) {
                    int now = q.remove();
                    if (visitied[now]) continue;
                    else {
                        visitied[now] = true;
                        for (int j = 0; j < N; j++) {
                            if (graph[now][j]) q.add(j);
                        }
                    }
                }
            }
        }
        System.out.println(unionCnt);
    }
}