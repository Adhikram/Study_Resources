const fs = require("fs");
data ={
  "problemsetQuestionList": {
    "total": 1212,
    "questions": [
      {
        "acRate": 62.415128804778895,
        "difficulty": "Easy",
        "freqBar": 22.633000232492165,
        "frontendQuestionId": "387",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "First Unique Character in a String",
        "titleSlug": "first-unique-character-in-a-string",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Queue",
            "id": "VG9waWNUYWdOb2RlOjM0",
            "slug": "queue"
          },
          {
            "name": "Counting",
            "id": "VG9waWNUYWdOb2RlOjYxMDYy",
            "slug": "counting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 87.62792930245315,
        "difficulty": "Easy",
        "freqBar": 22.481202257513395,
        "frontendQuestionId": "1431",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Kids With the Greatest Number of Candies",
        "titleSlug": "kids-with-the-greatest-number-of-candies",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 48.818106620225436,
        "difficulty": "Hard",
        "freqBar": 22.315913943392925,
        "frontendQuestionId": "123",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Best Time to Buy and Sell Stock III",
        "titleSlug": "best-time-to-buy-and-sell-stock-iii",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 66.58806881119169,
        "difficulty": "Easy",
        "freqBar": 22.154413290392657,
        "frontendQuestionId": "222",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Count Complete Tree Nodes",
        "titleSlug": "count-complete-tree-nodes",
        "topicTags": [
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          },
          {
            "name": "Bit Manipulation",
            "id": "VG9waWNUYWdOb2RlOjE5",
            "slug": "bit-manipulation"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 63.00346410376314,
        "difficulty": "Medium",
        "freqBar": 22.07644003691712,
        "frontendQuestionId": "178",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Rank Scores",
        "titleSlug": "rank-scores",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 27.19601110254747,
        "difficulty": "Hard",
        "freqBar": 21.9837375392895,
        "frontendQuestionId": "126",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Word Ladder II",
        "titleSlug": "word-ladder-ii",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Backtracking",
            "id": "VG9waWNUYWdOb2RlOjE0",
            "slug": "backtracking"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 76.45836787990642,
        "difficulty": "Easy",
        "freqBar": 21.98202962216742,
        "frontendQuestionId": "175",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Combine Two Tables",
        "titleSlug": "combine-two-tables",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 59.652602392106324,
        "difficulty": "Medium",
        "freqBar": 21.765999588722064,
        "frontendQuestionId": "103",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Binary Tree Zigzag Level Order Traversal",
        "titleSlug": "binary-tree-zigzag-level-order-traversal",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 52.324272427553296,
        "difficulty": "Medium",
        "freqBar": 21.75599696286196,
        "frontendQuestionId": "184",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Department Highest Salary",
        "titleSlug": "department-highest-salary",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 88.48488130208968,
        "difficulty": "Easy",
        "freqBar": 21.62037737297031,
        "frontendQuestionId": "2356",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Number of Unique Subjects Taught by Each Teacher",
        "titleSlug": "number-of-unique-subjects-taught-by-each-teacher",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 63.25169827200406,
        "difficulty": "Medium",
        "freqBar": 21.50455108426394,
        "frontendQuestionId": "684",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Redundant Connection",
        "titleSlug": "redundant-connection",
        "topicTags": [
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Union Find",
            "id": "VG9waWNUYWdOb2RlOjIz",
            "slug": "union-find"
          },
          {
            "name": "Graph",
            "id": "VG9waWNUYWdOb2RlOjI0",
            "slug": "graph"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 76.941649981529,
        "difficulty": "Easy",
        "freqBar": 21.4608862594903,
        "frontendQuestionId": "682",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Baseball Game",
        "titleSlug": "baseball-game",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Simulation",
            "id": "VG9waWNUYWdOb2RlOjYxMDU1",
            "slug": "simulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 70.42068202029002,
        "difficulty": "Medium",
        "freqBar": 21.431891705745297,
        "frontendQuestionId": "2352",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Equal Row and Column Pairs",
        "titleSlug": "equal-row-and-column-pairs",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          },
          {
            "name": "Simulation",
            "id": "VG9waWNUYWdOb2RlOjYxMDU1",
            "slug": "simulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 69.20106279582014,
        "difficulty": "Medium",
        "freqBar": 21.259828635489704,
        "frontendQuestionId": "1020",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Number of Enclaves",
        "titleSlug": "number-of-enclaves",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Union Find",
            "id": "VG9waWNUYWdOb2RlOjIz",
            "slug": "union-find"
          },
          {
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 61.35804049085063,
        "difficulty": "Medium",
        "freqBar": 21.217314221898587,
        "frontendQuestionId": "96",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Unique Binary Search Trees",
        "titleSlug": "unique-binary-search-trees",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 37.26676828639721,
        "difficulty": "Medium",
        "freqBar": 20.925130462073657,
        "frontendQuestionId": "907",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Sum of Subarray Minimums",
        "titleSlug": "sum-of-subarray-minimums",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Monotonic Stack",
            "id": "VG9waWNUYWdOb2RlOjYxMDU0",
            "slug": "monotonic-stack"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 51.23725765559543,
        "difficulty": "Easy",
        "freqBar": 20.876573490282674,
        "frontendQuestionId": "228",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Summary Ranges",
        "titleSlug": "summary-ranges",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 70.91685303184062,
        "difficulty": "Medium",
        "freqBar": 20.722014629671094,
        "frontendQuestionId": "791",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Custom Sort String",
        "titleSlug": "custom-sort-string",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 60.267395051404726,
        "difficulty": "Medium",
        "freqBar": 20.575890688638363,
        "frontendQuestionId": "36",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Valid Sudoku",
        "titleSlug": "valid-sudoku",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 35.35387545574012,
        "difficulty": "Easy",
        "freqBar": 20.56272233317667,
        "frontendQuestionId": "414",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Third Maximum Number",
        "titleSlug": "third-maximum-number",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 40.06477004443436,
        "difficulty": "Medium",
        "freqBar": 20.316081432106834,
        "frontendQuestionId": "373",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Find K Pairs with Smallest Sums",
        "titleSlug": "find-k-pairs-with-smallest-sums",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 57.19362178553197,
        "difficulty": "Easy",
        "freqBar": 20.249095309947652,
        "frontendQuestionId": "101",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Symmetric Tree",
        "titleSlug": "symmetric-tree",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 85.7499531293584,
        "difficulty": "Easy",
        "freqBar": 19.927524359440067,
        "frontendQuestionId": "2635",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Apply Transform Over Each Element in Array",
        "titleSlug": "apply-transform-over-each-element-in-array",
        "topicTags": [],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 63.583762399265474,
        "difficulty": "Medium",
        "freqBar": 19.87553006060078,
        "frontendQuestionId": "199",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Binary Tree Right Side View",
        "titleSlug": "binary-tree-right-side-view",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 85.02329569815636,
        "difficulty": "Easy",
        "freqBar": 19.602179206550066,
        "frontendQuestionId": "2418",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Sort the People",
        "titleSlug": "sort-the-people",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 64.34479136290695,
        "difficulty": "Easy",
        "freqBar": 19.42637012702823,
        "frontendQuestionId": "257",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Binary Tree Paths",
        "titleSlug": "binary-tree-paths",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Backtracking",
            "id": "VG9waWNUYWdOb2RlOjE0",
            "slug": "backtracking"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 40.38920792927845,
        "difficulty": "Medium",
        "freqBar": 19.253923335913,
        "frontendQuestionId": "97",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Interleaving String",
        "titleSlug": "interleaving-string",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 70.04325842696629,
        "difficulty": "Easy",
        "freqBar": 19.242543410014186,
        "frontendQuestionId": "872",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Leaf-Similar Trees",
        "titleSlug": "leaf-similar-trees",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 60.85437273994134,
        "difficulty": "Medium",
        "freqBar": 19.163284197977244,
        "frontendQuestionId": "1283",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Find the Smallest Divisor Given a Threshold",
        "titleSlug": "find-the-smallest-divisor-given-a-threshold",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 64.33445328155591,
        "difficulty": "Easy",
        "freqBar": 19.095898994101084,
        "frontendQuestionId": "303",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Range Sum Query - Immutable",
        "titleSlug": "range-sum-query-immutable",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          },
          {
            "name": "Prefix Sum",
            "id": "VG9waWNUYWdOb2RlOjYxMDY4",
            "slug": "prefix-sum"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 52.887300226068824,
        "difficulty": "Easy",
        "freqBar": 18.807189169016812,
        "frontendQuestionId": "455",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Assign Cookies",
        "titleSlug": "assign-cookies",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 46.87336308955021,
        "difficulty": "Easy",
        "freqBar": 18.458898409508745,
        "frontendQuestionId": "326",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Power of Three",
        "titleSlug": "power-of-three",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Recursion",
            "id": "VG9waWNUYWdOb2RlOjMx",
            "slug": "recursion"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 44.59027704023005,
        "difficulty": "Medium",
        "freqBar": 18.429995716405088,
        "frontendQuestionId": "735",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Asteroid Collision",
        "titleSlug": "asteroid-collision",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Simulation",
            "id": "VG9waWNUYWdOb2RlOjYxMDU1",
            "slug": "simulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 43.794582977946284,
        "difficulty": "Easy",
        "freqBar": 18.427687531315406,
        "frontendQuestionId": "367",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Valid Perfect Square",
        "titleSlug": "valid-perfect-square",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 48.66469432582055,
        "difficulty": "Easy",
        "freqBar": 18.222354808195245,
        "frontendQuestionId": "1731",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "The Number of Employees Which Report to Each Employee",
        "titleSlug": "the-number-of-employees-which-report-to-each-employee",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 43.97486230196008,
        "difficulty": "Hard",
        "freqBar": 18.20207882608177,
        "frontendQuestionId": "188",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Best Time to Buy and Sell Stock IV",
        "titleSlug": "best-time-to-buy-and-sell-stock-iv",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 71.35699105310897,
        "difficulty": "Easy",
        "freqBar": 18.15158952940818,
        "frontendQuestionId": "182",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Duplicate Emails",
        "titleSlug": "duplicate-emails",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 45.43057242030638,
        "difficulty": "Easy",
        "freqBar": 18.112516702815267,
        "frontendQuestionId": "2239",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Find Closest Number to Zero",
        "titleSlug": "find-closest-number-to-zero",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 17.6656367711275,
        "difficulty": "Medium",
        "freqBar": 17.87076292464967,
        "frontendQuestionId": "29",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Divide Two Integers",
        "titleSlug": "divide-two-integers",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Bit Manipulation",
            "id": "VG9waWNUYWdOb2RlOjE5",
            "slug": "bit-manipulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 64.44494736442597,
        "difficulty": "Easy",
        "freqBar": 17.844782594343915,
        "frontendQuestionId": "119",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Pascal's Triangle II",
        "titleSlug": "pascals-triangle-ii",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 48.368215878579534,
        "difficulty": "Easy",
        "freqBar": 17.796273085448906,
        "frontendQuestionId": "1978",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Employees Whose Manager Left the Company",
        "titleSlug": "employees-whose-manager-left-the-company",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 58.815604447433465,
        "difficulty": "Medium",
        "freqBar": 17.719204290249763,
        "frontendQuestionId": "309",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Best Time to Buy and Sell Stock with Cooldown",
        "titleSlug": "best-time-to-buy-and-sell-stock-with-cooldown",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 54.551952289178566,
        "difficulty": "Medium",
        "freqBar": 17.642798317182635,
        "frontendQuestionId": "1657",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Determine if Two Strings Are Close",
        "titleSlug": "determine-if-two-strings-are-close",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          },
          {
            "name": "Counting",
            "id": "VG9waWNUYWdOb2RlOjYxMDYy",
            "slug": "counting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 61.214915010534234,
        "difficulty": "Easy",
        "freqBar": 17.510650345584533,
        "frontendQuestionId": "448",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Find All Numbers Disappeared in an Array",
        "titleSlug": "find-all-numbers-disappeared-in-an-array",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 43.08537145741782,
        "difficulty": "Medium",
        "freqBar": 17.473252635613832,
        "frontendQuestionId": "662",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Maximum Width of Binary Tree",
        "titleSlug": "maximum-width-of-binary-tree",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 57.263148820292166,
        "difficulty": "Hard",
        "freqBar": 17.408183996856657,
        "frontendQuestionId": "297",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Serialize and Deserialize Binary Tree",
        "titleSlug": "serialize-and-deserialize-binary-tree",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 89.9442528077948,
        "difficulty": "Easy",
        "freqBar": 17.352788812354166,
        "frontendQuestionId": "1920",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Build Array from Permutation",
        "titleSlug": "build-array-from-permutation",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Simulation",
            "id": "VG9waWNUYWdOb2RlOjYxMDU1",
            "slug": "simulation"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 68.0783831265712,
        "difficulty": "Medium",
        "freqBar": 17.15458933167319,
        "frontendQuestionId": "102",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Binary Tree Level Order Traversal",
        "titleSlug": "binary-tree-level-order-traversal",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 63.78777907556692,
        "difficulty": "Easy",
        "freqBar": 17.018645038156173,
        "frontendQuestionId": "1137",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "N-th Tribonacci Number",
        "titleSlug": "n-th-tribonacci-number",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Memoization",
            "id": "VG9waWNUYWdOb2RlOjMz",
            "slug": "memoization"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 38.135073342109976,
        "difficulty": "Medium",
        "freqBar": 16.748110285300783,
        "frontendQuestionId": "678",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Valid Parenthesis String",
        "titleSlug": "valid-parenthesis-string",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 67.270563697094,
        "difficulty": "Medium",
        "freqBar": 16.547963600399857,
        "frontendQuestionId": "122",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Best Time to Buy and Sell Stock II",
        "titleSlug": "best-time-to-buy-and-sell-stock-ii",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 83.42339759669366,
        "difficulty": "Easy",
        "freqBar": 16.386117685095936,
        "frontendQuestionId": "1021",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Remove Outermost Parentheses",
        "titleSlug": "remove-outermost-parentheses",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 73.28199593934627,
        "difficulty": "Medium",
        "freqBar": 16.377874397419323,
        "frontendQuestionId": "230",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Kth Smallest Element in a BST",
        "titleSlug": "kth-smallest-element-in-a-bst",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 48.644909164840506,
        "difficulty": "Easy",
        "freqBar": 16.17427442765541,
        "frontendQuestionId": "111",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Minimum Depth of Binary Tree",
        "titleSlug": "minimum-depth-of-binary-tree",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 51.8921968708673,
        "difficulty": "Medium",
        "freqBar": 16.09414300796124,
        "frontendQuestionId": "1174",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Immediate Food Delivery II",
        "titleSlug": "immediate-food-delivery-ii",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 40.77319098492883,
        "difficulty": "Medium",
        "freqBar": 15.750051871755971,
        "frontendQuestionId": "43",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Multiply Strings",
        "titleSlug": "multiply-strings",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Simulation",
            "id": "VG9waWNUYWdOb2RlOjYxMDU1",
            "slug": "simulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 83.38229049043917,
        "difficulty": "Easy",
        "freqBar": 15.635787977215115,
        "frontendQuestionId": "1732",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Find the Highest Altitude",
        "titleSlug": "find-the-highest-altitude",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Prefix Sum",
            "id": "VG9waWNUYWdOb2RlOjYxMDY4",
            "slug": "prefix-sum"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 44.395188698761714,
        "difficulty": "Medium",
        "freqBar": 15.47830178323713,
        "frontendQuestionId": "180",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Consecutive Numbers",
        "titleSlug": "consecutive-numbers",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 37.17996603079246,
        "difficulty": "Medium",
        "freqBar": 15.47830178323713,
        "frontendQuestionId": "550",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Game Play Analysis IV",
        "titleSlug": "game-play-analysis-iv",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 55.14274286456606,
        "difficulty": "Medium",
        "freqBar": 15.294472281117235,
        "frontendQuestionId": "1679",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Max Number of K-Sum Pairs",
        "titleSlug": "max-number-of-k-sum-pairs",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 53.81537687475099,
        "difficulty": "Easy",
        "freqBar": 14.980127880758893,
        "frontendQuestionId": "234",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Palindrome Linked List",
        "titleSlug": "palindrome-linked-list",
        "topicTags": [
          {
            "name": "Linked List",
            "id": "VG9waWNUYWdOb2RlOjc=",
            "slug": "linked-list"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Recursion",
            "id": "VG9waWNUYWdOb2RlOjMx",
            "slug": "recursion"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 49.521220146340625,
        "difficulty": "Easy",
        "freqBar": 14.589246780068724,
        "frontendQuestionId": "203",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Remove Linked List Elements",
        "titleSlug": "remove-linked-list-elements",
        "topicTags": [
          {
            "name": "Linked List",
            "id": "VG9waWNUYWdOb2RlOjc=",
            "slug": "linked-list"
          },
          {
            "name": "Recursion",
            "id": "VG9waWNUYWdOb2RlOjMx",
            "slug": "recursion"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 64.73063052238365,
        "difficulty": "Easy",
        "freqBar": 14.370825086792399,
        "frontendQuestionId": "225",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Implement Stack using Queues",
        "titleSlug": "implement-stack-using-queues",
        "topicTags": [
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          },
          {
            "name": "Queue",
            "id": "VG9waWNUYWdOb2RlOjM0",
            "slug": "queue"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 45.41395373634649,
        "difficulty": "Easy",
        "freqBar": 14.056461609715612,
        "frontendQuestionId": "1211",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Queries Quality and Percentage",
        "titleSlug": "queries-quality-and-percentage",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 67.9384831299685,
        "difficulty": "Easy",
        "freqBar": 14.011091534766493,
        "frontendQuestionId": "1581",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Customer Who Visited but Did Not Make Any Transactions",
        "titleSlug": "customer-who-visited-but-did-not-make-any-transactions",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 42.276949893002566,
        "difficulty": "Easy",
        "freqBar": 13.37878339883897,
        "frontendQuestionId": "290",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Word Pattern",
        "titleSlug": "word-pattern",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 71.52901097563206,
        "difficulty": "Easy",
        "freqBar": 12.900945768555575,
        "frontendQuestionId": "509",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Fibonacci Number",
        "titleSlug": "fibonacci-number",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Recursion",
            "id": "VG9waWNUYWdOb2RlOjMx",
            "slug": "recursion"
          },
          {
            "name": "Memoization",
            "id": "VG9waWNUYWdOb2RlOjMz",
            "slug": "memoization"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 66.74119861413784,
        "difficulty": "Easy",
        "freqBar": 12.882045737239789,
        "frontendQuestionId": "232",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Implement Queue using Stacks",
        "titleSlug": "implement-queue-using-stacks",
        "topicTags": [
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          },
          {
            "name": "Queue",
            "id": "VG9waWNUYWdOb2RlOjM0",
            "slug": "queue"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 83.62060753192078,
        "difficulty": "Easy",
        "freqBar": 12.803852488556574,
        "frontendQuestionId": "1068",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Product Sales Analysis I",
        "titleSlug": "product-sales-analysis-i",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 33.24381010775644,
        "difficulty": "Medium",
        "freqBar": 12.447178057372472,
        "frontendQuestionId": "98",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Validate Binary Search Tree",
        "titleSlug": "validate-binary-search-tree",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 83.10052078950567,
        "difficulty": "Easy",
        "freqBar": 12.407963119552372,
        "frontendQuestionId": "1378",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Replace Employee ID With The Unique Identifier",
        "titleSlug": "replace-employee-id-with-the-unique-identifier",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 80.33251954846548,
        "difficulty": "Easy",
        "freqBar": 12.387276972842436,
        "frontendQuestionId": "700",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Search in a Binary Search Tree",
        "titleSlug": "search-in-a-binary-search-tree",
        "topicTags": [
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 40.33620660691153,
        "difficulty": "Medium",
        "freqBar": 12.09298712490906,
        "frontendQuestionId": "130",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Surrounded Regions",
        "titleSlug": "surrounded-regions",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Union Find",
            "id": "VG9waWNUYWdOb2RlOjIz",
            "slug": "union-find"
          },
          {
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 59.3972703503167,
        "difficulty": "Medium",
        "freqBar": 11.959482431589977,
        "frontendQuestionId": "2095",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Delete the Middle Node of a Linked List",
        "titleSlug": "delete-the-middle-node-of-a-linked-list",
        "topicTags": [
          {
            "name": "Linked List",
            "id": "VG9waWNUYWdOb2RlOjc=",
            "slug": "linked-list"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 37.983425611410624,
        "difficulty": "Easy",
        "freqBar": 11.562136584442067,
        "frontendQuestionId": "1251",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Average Selling Price",
        "titleSlug": "average-selling-price",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 72.75420431263774,
        "difficulty": "Easy",
        "freqBar": 11.391029442532975,
        "frontendQuestionId": "496",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Next Greater Element I",
        "titleSlug": "next-greater-element-i",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Monotonic Stack",
            "id": "VG9waWNUYWdOb2RlOjYxMDU0",
            "slug": "monotonic-stack"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 80.41907343938226,
        "difficulty": "Medium",
        "freqBar": 10.855317788624099,
        "frontendQuestionId": "237",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Delete Node in a Linked List",
        "titleSlug": "delete-node-in-a-linked-list",
        "topicTags": [
          {
            "name": "Linked List",
            "id": "VG9waWNUYWdOb2RlOjc=",
            "slug": "linked-list"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 51.58411481922964,
        "difficulty": "Easy",
        "freqBar": 10.173837664777755,
        "frontendQuestionId": "1071",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Greatest Common Divisor of Strings",
        "titleSlug": "greatest-common-divisor-of-strings",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 54.98828298316414,
        "difficulty": "Medium",
        "freqBar": 9.626448725050286,
        "frontendQuestionId": "40",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Combination Sum II",
        "titleSlug": "combination-sum-ii",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Backtracking",
            "id": "VG9waWNUYWdOb2RlOjE0",
            "slug": "backtracking"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 75.83601837737277,
        "difficulty": "Easy",
        "freqBar": 8.897513938589615,
        "frontendQuestionId": "577",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Employee Bonus",
        "titleSlug": "employee-bonus",
        "topicTags": [
          {
            "name": "Database",
            "id": "VG9waWNUYWdOb2RlOjYxMDQz",
            "slug": "database"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 28.989807499865204,
        "difficulty": "Easy",
        "freqBar": 8.490255253670258,
        "frontendQuestionId": "605",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Can Place Flowers",
        "titleSlug": "can-place-flowers",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 54.712052449828576,
        "difficulty": "Medium",
        "freqBar": 7.123431197711867,
        "frontendQuestionId": "155",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Min Stack",
        "titleSlug": "min-stack",
        "topicTags": [
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 61.804051934265104,
        "difficulty": "Medium",
        "freqBar": 5.269595349498474,
        "frontendQuestionId": "167",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Two Sum II - Input Array Is Sorted",
        "titleSlug": "two-sum-ii-input-array-is-sorted",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 81.90086513289066,
        "difficulty": "Easy",
        "freqBar": 4.0253655073346755,
        "frontendQuestionId": "2678",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Number of Senior Citizens",
        "titleSlug": "number-of-senior-citizens",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 44.9475740391009,
        "difficulty": "Medium",
        "freqBar": 3.7076716964267833,
        "frontendQuestionId": "151",
        "isFavor": false,
        "paidOnly": false,
        "status": "notac",
        "title": "Reverse Words in a String",
        "titleSlug": "reverse-words-in-a-string",
        "topicTags": [
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 63.40714451045444,
        "difficulty": "Medium",
        "freqBar": 1.8538358482133916,
        "frontendQuestionId": "1508",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Range Sum of Sorted Subarray Sums",
        "titleSlug": "range-sum-of-sorted-subarray-sums",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 58.48584511262547,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "133",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Clone Graph",
        "titleSlug": "clone-graph",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Breadth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIy",
            "slug": "breadth-first-search"
          },
          {
            "name": "Graph",
            "id": "VG9waWNUYWdOb2RlOjI0",
            "slug": "graph"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 55.60057106999818,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "159",
        "isFavor": false,
        "paidOnly": true,
        "status": "ac",
        "title": "Longest Substring with At Most Two Distinct Characters",
        "titleSlug": "longest-substring-with-at-most-two-distinct-characters",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 25.258099141826474,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "166",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Fraction to Recurring Decimal",
        "titleSlug": "fraction-to-recurring-decimal",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 42.92757290685366,
        "difficulty": "Hard",
        "freqBar": 0,
        "frontendQuestionId": "218",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "The Skyline Problem",
        "titleSlug": "the-skyline-problem",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Divide and Conquer",
            "id": "VG9waWNUYWdOb2RlOjEy",
            "slug": "divide-and-conquer"
          },
          {
            "name": "Binary Indexed Tree",
            "id": "VG9waWNUYWdOb2RlOjI4",
            "slug": "binary-indexed-tree"
          },
          {
            "name": "Segment Tree",
            "id": "VG9waWNUYWdOb2RlOjI5",
            "slug": "segment-tree"
          },
          {
            "name": "Line Sweep",
            "id": "VG9waWNUYWdOb2RlOjU2MTE5",
            "slug": "line-sweep"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          },
          {
            "name": "Ordered Set",
            "id": "VG9waWNUYWdOb2RlOjYxMDcw",
            "slug": "ordered-set"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 47.897253770024236,
        "difficulty": "Easy",
        "freqBar": 0,
        "frontendQuestionId": "231",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Power of Two",
        "titleSlug": "power-of-two",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
          },
          {
            "name": "Bit Manipulation",
            "id": "VG9waWNUYWdOb2RlOjE5",
            "slug": "bit-manipulation"
          },
          {
            "name": "Recursion",
            "id": "VG9waWNUYWdOb2RlOjMx",
            "slug": "recursion"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 47.68097622636006,
        "difficulty": "Easy",
        "freqBar": 0,
        "frontendQuestionId": "246",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Strobogrammatic Number",
        "titleSlug": "strobogrammatic-number",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 65.948521331804,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "249",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Group Shifted Strings",
        "titleSlug": "group-shifted-strings",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 49.621309939987746,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "251",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Flatten 2D Vector",
        "titleSlug": "flatten-2d-vector",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
          },
          {
            "name": "Iterator",
            "id": "VG9waWNUYWdOb2RlOjYxMDY0",
            "slug": "iterator"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 50.81298796638922,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "259",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "3Sum Smaller",
        "titleSlug": "3sum-smaller",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 67.5894588860107,
        "difficulty": "Easy",
        "freqBar": 0,
        "frontendQuestionId": "266",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Palindrome Permutation",
        "titleSlug": "palindrome-permutation",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Bit Manipulation",
            "id": "VG9waWNUYWdOb2RlOjE5",
            "slug": "bit-manipulation"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 51.26308975066935,
        "difficulty": "Easy",
        "freqBar": 0,
        "frontendQuestionId": "270",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Closest Binary Search Tree Value",
        "titleSlug": "closest-binary-search-tree-value",
        "topicTags": [
          {
            "name": "Binary Search",
            "id": "VG9waWNUYWdOb2RlOjEx",
            "slug": "binary-search"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 59.36658710042572,
        "difficulty": "Hard",
        "freqBar": 0,
        "frontendQuestionId": "272",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Closest Binary Search Tree Value II",
        "titleSlug": "closest-binary-search-tree-value-ii",
        "topicTags": [
          {
            "name": "Two Pointers",
            "id": "VG9waWNUYWdOb2RlOjk=",
            "slug": "two-pointers"
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Tree",
            "id": "VG9waWNUYWdOb2RlOjIw",
            "slug": "tree"
          },
          {
            "name": "Depth-First Search",
            "id": "VG9waWNUYWdOb2RlOjIx",
            "slug": "depth-first-search"
          },
          {
            "name": "Binary Search Tree",
            "id": "VG9waWNUYWdOb2RlOjMw",
            "slug": "binary-search-tree"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          },
          {
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 46.88876202903278,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "276",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Paint Fence",
        "titleSlug": "paint-fence",
        "topicTags": [
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 67.78124528586514,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "280",
        "isFavor": false,
        "paidOnly": true,
        "status": null,
        "title": "Wiggle Sort",
        "titleSlug": "wiggle-sort",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      }
    ]
  }
};

const company = "Google";
function transformedData(data) {
  const transformedData = data.problemsetQuestionList.questions.map(
    (question) => ({
      difficulty: question.difficulty,
      freqBar: question.freqBar,
      status: question.status,
      title: question.title,
      link: `https://leetcode.com/problems/${question.titleSlug}/description/`,
      topicTags: question.topicTags.map((tag) => tag.name),
      company: company,
    })
  );

  const headers = [
    "difficulty",
    "freqBar",
    "status",
    "title",
    "link",
    "topicTags",
    "company",
  ];

  const csvRows = transformedData.map((row) =>
    headers.map((header) => JSON.stringify(row[header] || "")).join(",")
  );

  const csvContent = csvRows.join("\n");
  const filePath = company + ".csv";

  if (fs.existsSync(filePath)) {
    fs.appendFileSync(filePath, "\n" + csvContent);
  } else {
    const headerRow = headers.join(",") + "\n";
    fs.writeFileSync(filePath, headerRow + csvContent);
  }

  console.log("CSV file created successfully for " + company + "!");
}

// Assuming `data` is defined elsewhere in your code
transformedData(data);