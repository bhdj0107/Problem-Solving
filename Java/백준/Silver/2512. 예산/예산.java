import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> budgets = new ArrayList<>();

        for (int i = 0; i < N; i++) budgets.add(Integer.parseInt(st.nextToken()));
        Collections.sort(budgets);
        int maxBudget = Integer.parseInt(br.readLine());
        
        int left = 0; int right = budgets.get(N - 1) + 1;
        while (true) {
            if (left == right - 1) break;
            else {
                int middle = (right + left) / 2;

                // chk is able

                // right 를 줄여야 하는 경우 -> budget sum 이 max budget 초과인 경우
                // left 를 늘려야 하는 경우 -> budget sum 이 max budget 이하인 경우

                int budgetsum = 0;
                for (int i = 0; i < N; i++) {
                    int nowBudget = budgets.get(i);
                    if (nowBudget <= middle) {
                        budgetsum += nowBudget;
                    } else {
                        budgetsum += middle * (N - i);
                        break;
                    }
                }

                if (budgetsum <= maxBudget) {
                    left = middle;
                } else {
                    right = middle;
                }
            }
        }
        System.out.println(left);
    }
}