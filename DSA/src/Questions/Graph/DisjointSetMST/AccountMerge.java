package Questions.Graph.DisjointSetMST;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AccountMerge {
    static List<List<String>> accountsMerge(List<List<String>> details) {
        // Get the number of accounts
        int n = details.size();

        // Initialize DisjointSet to keep track of connected components
        DisjointSet ds = new DisjointSet(n);

        // HashMap to map email to its corresponding node index
        HashMap<String, Integer> mapMailNode = new HashMap<>();

        // Iterate through each account
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < details.get(i).size(); j++) {
                String mail = details.get(i).get(j);
                // If the email is encountered for the first time
                if (!mapMailNode.containsKey(mail)) {
                    mapMailNode.put(mail, i); // Map email to its node index
                } else {
                    // If the email is already mapped to a node, merge the nodes
                    ds.unionBySize(i, mapMailNode.get(mail));
                }
            }
        }

        // Array of lists to store merged emails for each node
        ArrayList<String>[] mergedMail = new ArrayList[n];
        for (int i = 0; i < n; i++)
            mergedMail[i] = new ArrayList<>();

        // Populate mergedMail with emails for each connected component
        for (Map.Entry<String, Integer> entry : mapMailNode.entrySet()) {
            String mail = entry.getKey();
            int node = ds.findUPar(entry.getValue());
            mergedMail[node].add(mail);
        }

        // Prepare the final merged accounts
        List<List<String>> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (mergedMail[i].isEmpty())
                continue; // Skip if no emails in this component
            Collections.sort(mergedMail[i]); // Sort the emails
            List<String> temp = new ArrayList<>();
            temp.add(details.get(i).get(0)); // Add the name of the account holder
            temp.addAll(mergedMail[i]); // Add all merged emails
            ans.add(temp); // Add the account details to the final list
        }
        return ans;
    }

    // Time Complexity:

    // O(N+E) + O(E*4ɑ) + O(N*(ElogE + E)) where N = no. of indices
    // or nodes and E = no. of emails. The first term is for visiting all the
    // emails. The second term is for merging the accounts. And the third term is
    // for sorting the emails and storing them in the answer array.

    // Space Complexity:

    // O(N)+ O(N) +O(2N) ~ O(N) where N = no. of nodes/indices. The first and second
    // space is for the ‘mergedMail’ and the ‘ans’ array. The last term is for the
    // parent and size array used inside the Disjoint set data structure.

    public static void main(String[] args) {
        // Sample account details
        List<List<String>> accounts = Arrays.asList(
                Arrays.asList("John", "j1@com", "j2@com", "j3@com"),
                Arrays.asList("John", "j4@com"),
                Arrays.asList("Raj", "r1@com", "r2@com"),
                Arrays.asList("John", "j1@com", "j5@com"),
                Arrays.asList("Raj", "r2@com", "r3@com"),
                Arrays.asList("Mary", "m1@com"));

        // Merge accounts
        List<List<String>> mergedAccounts = accountsMerge(accounts);

        // Print merged accounts
        for (List<String> account : mergedAccounts) {
            System.out.print(account.get(0) + ": ");
            for (int i = 1; i < account.size(); i++) {
                System.out.print(account.get(i) + " ");
            }
            System.out.println();
        }
    }
}
