import java.io.*;
import java.util.*;

class Node {
    public Node left;
    public Node right;
    public String value;
    Node(String value) {
        this.value = value;
    }

    void preOrder(StringBuilder sb) {
        sb.append(this.value);
        if (left != null) left.preOrder(sb);
        if (right != null) right.preOrder(sb);
    }

    void inOrder(StringBuilder sb) {
        if (left != null) left.inOrder(sb);
        sb.append(this.value);
        if (right != null) right.inOrder(sb);
    }

    void postOrder(StringBuilder sb) {
        if (left != null) left.postOrder(sb);
        if (right != null) right.postOrder(sb);
        sb.append(this.value);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Node[] nodes = new Node[N];
        String abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < N; i++) nodes[i] = new Node(abcd.substring(i, i + 1));
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int targetNode = st.nextToken().charAt(0) - 'A';
            String tmpStr = st.nextToken();
            if (!tmpStr.equals(".")) {
                nodes[targetNode].left = nodes[tmpStr.charAt(0) - 'A'];
            }
            tmpStr = st.nextToken();
            if (!tmpStr.equals(".")) {
                nodes[targetNode].right = nodes[tmpStr.charAt(0) - 'A'];
            }
        }
        StringBuilder sb = new StringBuilder();
        nodes[0].preOrder(sb);
        System.out.println(sb.toString());

        sb = new StringBuilder();
        nodes[0].inOrder(sb);
        System.out.println(sb.toString());

        
        sb = new StringBuilder();
        nodes[0].postOrder(sb);
        System.out.println(sb.toString());
    }
}