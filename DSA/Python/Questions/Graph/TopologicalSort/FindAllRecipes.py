"""
# Question: Find All Possible Recipes from Given Supplies
# Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# Time Complexity: O(V + E) where V is recipes + ingredients
# Space Complexity: O(V + E)

# Algorithm:
# 1. Build dependency graph for recipes
# 2. Topological sort with supplies check
# 3. Return possible recipes
"""

from collections import defaultdict, deque


class FindAllRecipes:
    def find_all_recipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        # Build graph and in-degree count
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        supplies_set = set(supplies)
        recipes_set = set(recipes)

        for recipe, recipe_ingredients in zip(recipes, ingredients):
            for ingredient in recipe_ingredients:
                if ingredient not in supplies_set:
                    graph[ingredient].append(recipe)
                    in_degree[recipe] += 1

        # Start with recipes that have all ingredients in supplies
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        possible_recipes = []

        while queue:
            recipe = queue.popleft()
            possible_recipes.append(recipe)

            for next_recipe in graph[recipe]:
                in_degree[next_recipe] -= 1
                if in_degree[next_recipe] == 0:
                    queue.append(next_recipe)

        return possible_recipes


def main():
    solution = FindAllRecipes()
    recipes = ["bread", "sandwich"]
    ingredients = [["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]
    print(solution.find_all_recipes(recipes, ingredients, supplies))


if __name__ == "__main__":
    main()
