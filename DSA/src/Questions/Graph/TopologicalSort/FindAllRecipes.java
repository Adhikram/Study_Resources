package Questions.Graph.TopologicalSort;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
/*
 2115. Find All Possible Recipes from Given Supplies
Solved
Medium
Topics
Companies
Hint
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
 */

//  Time complexity: O(V+E)
//  Space complexity: O(V+E)

public class FindAllRecipes {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        HashSet<String> sup = new HashSet<>();
        HashMap<String, Integer> index = new HashMap<>();
        HashMap<String, List<String>> map = new HashMap<>();

        // create hashset of supplies
        for (String s : supplies) {
            sup.add(s);
        }

        // store index of all recipes
        for (int i = 0; i < recipes.length; i++) {
            index.put(recipes[i], i);
        }

        int[] inDegree = new int[recipes.length];
        // create a mapping of all the recipes that are Ingredients as well
        // to the recipes they are ingredients for
        for (int i = 0; i < recipes.length; i++) {
            for (String need : ingredients.get(i)) {
                // We are skipping the raw ingredients
                if (sup.contains(need))
                    continue;

                map.putIfAbsent(need, new ArrayList<String>());
                // add the recipe as an ingredient for the recipe
                System.out.println("Need: " + need + " Recipe: " + recipes[i]);
                map.get(need).add(recipes[i]);
                inDegree[i]++;
            }
        }

        LinkedList<Integer> q = new LinkedList<>();
        // add all the recipes with indegree 0 to the queue
        for (int i = 0; i < recipes.length; i++) {
            if (inDegree[i] == 0) {
                q.add(i);
            }
        }

        System.out.println("Queue: " + q.toString());
        List<String> cooked = new ArrayList<>();
        while (!q.isEmpty()) {
            int i = q.poll();
            System.out.println("Cooked Recipe: " + recipes[i]);
            cooked.add(recipes[i]);

            if (!map.containsKey(recipes[i])) {
                // if the map does not contain this recipe, this means
                // this recipe is not an ingredient for any other recipe
                // and no further processing is required
                continue;
            }

            for (String recipe : map.get(recipes[i])) {
                System.out.println("Recipe: " + recipe);
                if (--inDegree[index.get(recipe)] == 0) {
                    System.out.println("Adding: " + recipe);
                    q.add(index.get(recipe));
                }
            }
        }

        return cooked;
    }

    public static void main(String[] args) {
        FindAllRecipes findAllRecipes = new FindAllRecipes();

        // Example 1
        String[] recipes1 = { "bread" };
        List<List<String>> ingredients1 = new ArrayList<>();
        ingredients1.add(Arrays.asList("yeast", "flour"));
        String[] supplies1 = { "yeast", "flour", "corn" };
        System.out.println(
                "-------------------------------------------------------------------------------------------------");
        System.out.println(findAllRecipes.findAllRecipes(recipes1, ingredients1, supplies1)); // Output: ["bread"]
        System.out.println(
                "-------------------------------------------------------------------------------------------------");

        // Example 2
        String[] recipes2 = { "bread", "sandwich" };
        List<List<String>> ingredients2 = new ArrayList<>();
        ingredients2.add(Arrays.asList("yeast", "flour"));
        ingredients2.add(Arrays.asList("bread", "meat"));
        String[] supplies2 = { "yeast", "flour", "meat" };
        System.out.println(
                "-------------------------------------------------------------------------------------------------");
        System.out.println(findAllRecipes.findAllRecipes(recipes2, ingredients2, supplies2)); // Output: ["bread",
                                                                                              // "sandwich"]
        System.out.println(
                "-------------------------------------------------------------------------------------------------");

        // Example 3
        String[] recipes3 = { "bread", "sandwich", "burger" };
        List<List<String>> ingredients3 = new ArrayList<>();
        ingredients3.add(Arrays.asList("yeast", "flour"));
        ingredients3.add(Arrays.asList("bread", "meat"));
        ingredients3.add(Arrays.asList("sandwich", "meat", "bread"));
        String[] supplies3 = { "yeast", "flour", "meat" };
        System.out.println(
                "-------------------------------------------------------------------------------------------------");
        System.out.println(findAllRecipes.findAllRecipes(recipes3, ingredients3, supplies3)); // Output: ["bread",
                                                                                              // "sandwich", "burger"]
        System.out.println(
                "-------------------------------------------------------------------------------------------------");
    }
}
