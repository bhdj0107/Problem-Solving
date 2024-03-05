import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.util.*;

public class Main {
    static InputStreamReader reader = new InputStreamReader(System.in);
    static BufferedReader br = new BufferedReader(reader);

    static OutputStreamWriter writer = new OutputStreamWriter(System.out);
    static BufferedWriter bw = new BufferedWriter(writer);

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        String prompt = "";

        prompt += "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n";
        prompt += "\"재귀함수가 뭔가요?\"\n";
        prompt += "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n";
        prompt += "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n";
        prompt += "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";

        bwPrint(prompt);
        recur(N, N - 1);
        bwPrint("라고 답변하였지.");

        bw.flush();
        bw.close();
    }

    static void bwPrint(String s) throws IOException {
        bw.write(s + "\n");
    }
    static void recur(int N, int C) throws IOException {
        if (C == 0) {
            String tabs = "";
            for (int i = 0; i < N; i++) tabs += "____";
            String output[] = new String[3];
            output[0] = "\"재귀함수가 뭔가요?\"";
            output[1] = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
            output[2] = "라고 답변하였지.";
            for (int i = 0; i < 3; i++) {
                bwPrint(tabs + output[i]);
            }
        }
        else {
            String tabs = "";
            for (int i = 0; i < N - C; i++) tabs += "____";

            String output[] = new String[4];
            
            output[0] = "\"재귀함수가 뭔가요?\"";
            output[1] = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
            output[2] = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
            output[3] = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";

            for (int i = 0; i < 4; i++) {
                bwPrint(tabs + output[i]);
            }

            recur(N, C - 1);

            bwPrint(tabs + "라고 답변하였지.");
        }
    }
}