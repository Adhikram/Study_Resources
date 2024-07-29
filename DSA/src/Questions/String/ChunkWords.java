package Questions.String;

import java.util.ArrayList;

class ChunkWords {

    public static ArrayList<String> solve(String str) {
        if (str == null) {
            return new ArrayList<>();
        }
        int space = 0;
        int start = 0;
        int n = str.length();
        ArrayList<String> result = new ArrayList<>();
        int limit = 160;
        if (n <= limit) {
            result.add(str);
            return result;
        }
        // O(N)
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == ' ') {
                space = i;
            }

            int buffer = 6;
            if (i - start >= limit - buffer) {

                // Reset the Starts
                if (i < n - 1 && str.charAt(i) != ' ') {
                    // Take upto the space
                    result.add(str.substring(start, space));
                    start = space + 1;
                } else {
                    // Take upto i
                    result.add(str.substring(start, i));
                    start = i + 1;
                }
            }
        }

        if (result.size() == 1) {
            return result;
        }
        // O(n)
        for (int i = 0; i < result.size(); i++) {
            String index = " (" + i + "/" + result.size() + ")";
            // System.out.println(index);
            result.set(i, result.get(i) + index);
        }

        return result;
    }

    public static void main(String[] args) {
        String str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.";
        ArrayList<String> result = solve(str);
        System.out.println(result);
        // Null
        result = solve(null);
        System.out.println(result);
        str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem. Proin nunc ex, suscipit sagittis tempor ac, tempor ut ante. Phasellus in dapibus nam.";
        result = solve(str);
        System.out.println(result);
        str = "Lorem ipsum dolor sit amet";
        result = solve(str);
        System.out.println(result);
    }

}