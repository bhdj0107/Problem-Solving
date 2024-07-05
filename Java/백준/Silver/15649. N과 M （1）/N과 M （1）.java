import java.io.*;
import java.util.*;

class Stack {
    public int[] container;
    public int length = 0;
    Stack (int size) {
        container = new int[size];
    }

    public void push(int n) {
        container[length] = n;
        length += 1;
    }

    public int pop() {
        int t = container[length];
        length -= 1;
        return t;
    }

    public String print() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length - 1; i++) {
            sb.append(Integer.toString(container[i]) + " ");
        }
        sb.append(Integer.toString(container[length - 1]));
        return sb.toString();
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static Stack stack = new Stack(10);
    static boolean[] isPicked = new boolean[10];
    static int N, M;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        backtracking(M);
        bw.flush();
        bw.close();
    }

    static void backtracking(int D) throws IOException {
        if (D == 0) {
            bw.write(stack.print() + "\n");
        } else {
            for (int i = 1; i <= N; i++) {
                if (isPicked[i]) continue;
                isPicked[i] = true;
                stack.push(i);
                backtracking(D - 1);
                stack.pop();
                isPicked[i] = false;
            }
        }
    }
}