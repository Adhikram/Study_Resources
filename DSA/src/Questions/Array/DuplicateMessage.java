package Questions.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

// if the message is duplicated anytime in the 10 sec duration remove all occurances and dont print any one , Not even the 1st one . 
// INPUT : t1 ,t5 , f8 , t11 ,t12 ,t21,t23 ,g32,t46
// Output :  f8  t23 g32  t46
public class DuplicateMessage {

    public static ArrayList<String> solve(String[] messages) {
        int n = messages.length;
        ArrayList<String> result = new ArrayList<>();
        HashMap<String, Integer> hash = new HashMap<>();
        // Assumption: messages are identified bye the first character
        for (int i = 0; i < n; i++) {
            String message = messages[i];
            String key = message.substring(0, 1);
            Integer timeStr = Integer.parseInt(message.substring(1));
            System.out.println("Time: " + timeStr + " key: " + key);
            if (hash.containsKey(key)) {
                int prevTime = hash.get(key);
                System.out.println("Prev Time: " + prevTime + " Time: " + timeStr);
                if (timeStr - prevTime > 10) {
                    System.out.print(message + " ");
                    result.add(message);
                }
            } else {

            }
            hash.put(key, timeStr);
        }
        return result;
    }

    public static void main(String[] args) {
        String[] messages = { "t1", "t5", "f8", "t11", "t12", "t21", "t23", "g32", "t46" };
        ArrayList<String> result = solve(messages);
        System.out.println("Result: " + result);
    }
}
