package Questions.String;

public class QueryWildCardMatch {
    public static void main(String[] args) {
        printTestCase("hello world", "hel?lo", true);
        printTestCase("hello world", "ll?o", true);
        printTestCase("hello world", "hell?l?l?o?o?", true);
        printTestCase("hello world", "hell?o?o", true);
        printTestCase("hello world", "hell?lo", true);
        printTestCase("hello world", "world?", true);
        printTestCase("hello world", "worldd?", true);
        printTestCase("hello world", ".?ell?l?l?o?o?", true);
    }
    private static void printTestCase(String text, String query, boolean expected) {
        boolean result = question_wildcard_match(text, query);
        System.out.println("Input: text = \"" + text + "\", query = \"" + query + "\"");
        System.out.println("Expected: " + expected + ", Actual: " + result);
        assert result == expected : "Test case failed for input: text = \"" + text + "\", query = \"" + query + "\"";
    }

    public static boolean helper(String text, String query, int tIndex, int qIndex) {

        if (qIndex == query.length()) {
            return true;
        }

        if (tIndex == text.length()) {
            return false;
        }

        // 'x?'
        char queryChar = query.charAt(qIndex);
        if (qIndex + 1 < query.length() && query.charAt(qIndex + 1) == '?') {
            // Skip the next char 0
            if (helper(text, query, tIndex, qIndex + 2)) {
                return true;
            }
            // Taking this char
            if (text.charAt(tIndex) == queryChar || queryChar == '.') {
                return helper(text, query, tIndex + 1, qIndex + 2);
            }
            return helper(text, query, tIndex + 1, 0);
        }
        if (text.charAt(tIndex) == query.charAt(qIndex) || query.charAt(qIndex) == '.') {
            return helper(text, query, tIndex + 1, qIndex + 1);
        }else{
            return helper(text, query, tIndex + 1, 0);
        }

    }

    public static boolean question_wildcard_match(String text, String query) {
        // Write your code here
        int qL = query.length();

        if (qL == 0)
            return true;
        if (query.startsWith("?") || query.contains("??")) {
            return false;
        }

        return helper(text, query, 0, 0);
    }
}
