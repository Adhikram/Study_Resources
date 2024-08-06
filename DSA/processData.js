const fs = require("fs");
data ={
  "problemsetQuestionList": {
    "total": 63,
    "questions": [
      {
        "acRate": 43.070100952920086,
        "difficulty": "Hard",
        "freqBar": 100,
        "frontendQuestionId": "2499",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Minimum Total Cost to Make Arrays Unequal",
        "titleSlug": "minimum-total-cost-to-make-arrays-unequal",
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
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Counting",
            "id": "VG9waWNUYWdOb2RlOjYxMDYy",
            "slug": "counting"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 42.66127813869164,
        "difficulty": "Hard",
        "freqBar": 89.86579534076822,
        "frontendQuestionId": "1703",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Minimum Adjacent Swaps for K Consecutive Ones",
        "titleSlug": "minimum-adjacent-swaps-for-k-consecutive-ones",
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
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
          },
          {
            "name": "Prefix Sum",
            "id": "VG9waWNUYWdOb2RlOjYxMDY4",
            "slug": "prefix-sum"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 62.97707762350223,
        "difficulty": "Hard",
        "freqBar": 88.36840287453334,
        "frontendQuestionId": "632",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Smallest Range Covering Elements from K Lists",
        "titleSlug": "smallest-range-covering-elements-from-k-lists",
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
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
          },
          {
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
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
        "acRate": 57.83902146856643,
        "difficulty": "Medium",
        "freqBar": 86.1565347906342,
        "frontendQuestionId": "934",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Shortest Bridge",
        "titleSlug": "shortest-bridge",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 13.902455471105588,
        "difficulty": "Hard",
        "freqBar": 75.29602523516525,
        "frontendQuestionId": "420",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Strong Password Checker",
        "titleSlug": "strong-password-checker",
        "topicTags": [
          {
            "name": "String",
            "id": "VG9waWNUYWdOb2RlOjEw",
            "slug": "string"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 30.53742943031014,
        "difficulty": "Hard",
        "freqBar": 64.43551567969627,
        "frontendQuestionId": "321",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Create Maximum Number",
        "titleSlug": "create-maximum-number",
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
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          },
          {
            "name": "Greedy",
            "id": "VG9waWNUYWdOb2RlOjE3",
            "slug": "greedy"
          },
          {
            "name": "Monotonic Stack",
            "id": "VG9waWNUYWdOb2RlOjYxMDU0",
            "slug": "monotonic-stack"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 49.97042295178941,
        "difficulty": "Hard",
        "freqBar": 62.97233710965564,
        "frontendQuestionId": "2141",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Maximum Running Time of N Computers",
        "titleSlug": "maximum-running-time-of-n-computers",
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
        "acRate": 58.52262220304506,
        "difficulty": "Medium",
        "freqBar": 61.16635313249812,
        "frontendQuestionId": "1366",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Rank Teams by Votes",
        "titleSlug": "rank-teams-by-votes",
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
          },
          {
            "name": "Counting",
            "id": "VG9waWNUYWdOb2RlOjYxMDYy",
            "slug": "counting"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 66.5712983016072,
        "difficulty": "Hard",
        "freqBar": 60.74214323084398,
        "frontendQuestionId": "2551",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Put Marbles in Bags",
        "titleSlug": "put-marbles-in-bags",
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
        "acRate": 38.35764562707627,
        "difficulty": "Hard",
        "freqBar": 60.61841754394383,
        "frontendQuestionId": "719",
        "isFavor": false,
        "paidOnly": false,
        "status": "notac",
        "title": "Find K-th Smallest Pair Distance",
        "titleSlug": "find-k-th-smallest-pair-distance",
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
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 60.310696450464995,
        "difficulty": "Medium",
        "freqBar": 60.02242602007377,
        "frontendQuestionId": "1760",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Minimum Limit of Balls in a Bag",
        "titleSlug": "minimum-limit-of-balls-in-a-bag",
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
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 71.85939269506841,
        "difficulty": "Hard",
        "freqBar": 53.55734272882241,
        "frontendQuestionId": "1463",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Cherry Pickup II",
        "titleSlug": "cherry-pickup-ii",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 65.23093371500751,
        "difficulty": "Medium",
        "freqBar": 52.65596662751385,
        "frontendQuestionId": "983",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Minimum Cost For Tickets",
        "titleSlug": "minimum-cost-for-tickets",
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
        "acRate": 53.125670528913204,
        "difficulty": "Hard",
        "freqBar": 50.953531730185695,
        "frontendQuestionId": "330",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Patching Array",
        "titleSlug": "patching-array",
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
        "acRate": 38.977304759220175,
        "difficulty": "Hard",
        "freqBar": 45.00840223417041,
        "frontendQuestionId": "480",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Sliding Window Median",
        "titleSlug": "sliding-window-median",
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
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
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
        "acRate": 62.72017707882418,
        "difficulty": "Medium",
        "freqBar": 44.62680369126128,
        "frontendQuestionId": "2385",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Amount of Time for Binary Tree to Be Infected",
        "titleSlug": "amount-of-time-for-binary-tree-to-be-infected",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
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
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 34.14649288815434,
        "difficulty": "Medium",
        "freqBar": 44.30499009719687,
        "frontendQuestionId": "556",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Next Greater Element III",
        "titleSlug": "next-greater-element-iii",
        "topicTags": [
          {
            "name": "Math",
            "id": "VG9waWNUYWdOb2RlOjg=",
            "slug": "math"
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
        "hasVideoSolution": false
      },
      {
        "acRate": 71.77818896395426,
        "difficulty": "Easy",
        "freqBar": 43.86333075202443,
        "frontendQuestionId": "1598",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Crawler Log Folder",
        "titleSlug": "crawler-log-folder",
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
          },
          {
            "name": "Stack",
            "id": "VG9waWNUYWdOb2RlOjE1",
            "slug": "stack"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 44.590052126467576,
        "difficulty": "Medium",
        "freqBar": 43.80119561485646,
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
        "acRate": 59.5002232918176,
        "difficulty": "Hard",
        "freqBar": 43.50107875623878,
        "frontendQuestionId": "312",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Burst Balloons",
        "titleSlug": "burst-balloons",
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
        "acRate": 55.41502745083511,
        "difficulty": "Medium",
        "freqBar": 42.49875099597301,
        "frontendQuestionId": "486",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Predict the Winner",
        "titleSlug": "predict-the-winner",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
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
            "name": "Game Theory",
            "id": "VG9waWNUYWdOb2RlOjYxMDcz",
            "slug": "game-theory"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 38.3272900747553,
        "difficulty": "Hard",
        "freqBar": 40.7305421956207,
        "frontendQuestionId": "174",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Dungeon Game",
        "titleSlug": "dungeon-game",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 54.363009247000484,
        "difficulty": "Hard",
        "freqBar": 39.75890243648526,
        "frontendQuestionId": "1235",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Maximum Profit in Job Scheduling",
        "titleSlug": "maximum-profit-in-job-scheduling",
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
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
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
        "acRate": 50.94927520602332,
        "difficulty": "Medium",
        "freqBar": 38.62693704834548,
        "frontendQuestionId": "718",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Maximum Length of Repeated Subarray",
        "titleSlug": "maximum-length-of-repeated-subarray",
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
          },
          {
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
          },
          {
            "name": "Rolling Hash",
            "id": "VG9waWNUYWdOb2RlOjU2NTk4",
            "slug": "rolling-hash"
          },
          {
            "name": "Hash Function",
            "id": "VG9waWNUYWdOb2RlOjYxMDY1",
            "slug": "hash-function"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 46.138223527783715,
        "difficulty": "Medium",
        "freqBar": 37.9905151720061,
        "frontendQuestionId": "437",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Path Sum III",
        "titleSlug": "path-sum-iii",
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
        "acRate": 70.09885275539209,
        "difficulty": "Medium",
        "freqBar": 37.02301659069714,
        "frontendQuestionId": "1011",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Capacity To Ship Packages Within D Days",
        "titleSlug": "capacity-to-ship-packages-within-d-days",
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
        "acRate": 47.03956260228207,
        "difficulty": "Medium",
        "freqBar": 35.876147123444994,
        "frontendQuestionId": "221",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Maximal Square",
        "titleSlug": "maximal-square",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 35.186481951248304,
        "difficulty": "Medium",
        "freqBar": 35.12197213700633,
        "frontendQuestionId": "3",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Longest Substring Without Repeating Characters",
        "titleSlug": "longest-substring-without-repeating-characters",
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
        "acRate": 63.3356759899688,
        "difficulty": "Medium",
        "freqBar": 32.23572626202453,
        "frontendQuestionId": "116",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Populating Next Right Pointers in Each Node",
        "titleSlug": "populating-next-right-pointers-in-each-node",
        "topicTags": [
          {
            "name": "Linked List",
            "id": "VG9waWNUYWdOb2RlOjc=",
            "slug": "linked-list"
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
            "name": "Binary Tree",
            "id": "VG9waWNUYWdOb2RlOjYxMDU3",
            "slug": "binary-tree"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 65.52246995570819,
        "difficulty": "Easy",
        "freqBar": 31.871080229157233,
        "frontendQuestionId": "1046",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Last Stone Weight",
        "titleSlug": "last-stone-weight",
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
        "acRate": 51.23233833050639,
        "difficulty": "Hard",
        "freqBar": 31.45211285545425,
        "frontendQuestionId": "85",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Maximal Rectangle",
        "titleSlug": "maximal-rectangle",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
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
        "acRate": 35.25607844387911,
        "difficulty": "Medium",
        "freqBar": 29.90994992308369,
        "frontendQuestionId": "91",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Decode Ways",
        "titleSlug": "decode-ways",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 46.58233242259749,
        "difficulty": "Medium",
        "freqBar": 27.311286900522468,
        "frontendQuestionId": "416",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Partition Equal Subset Sum",
        "titleSlug": "partition-equal-subset-sum",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 48.42767916623878,
        "difficulty": "Medium",
        "freqBar": 27.293924375016992,
        "frontendQuestionId": "875",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Koko Eating Bananas",
        "titleSlug": "koko-eating-bananas",
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
        "acRate": 62.706733379931634,
        "difficulty": "Hard",
        "freqBar": 27.246749023819834,
        "frontendQuestionId": "42",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Trapping Rain Water",
        "titleSlug": "trapping-rain-water",
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
        "acRate": 59.65192570179034,
        "difficulty": "Medium",
        "freqBar": 26.433411476784812,
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
        "acRate": 47.23287066633603,
        "difficulty": "Medium",
        "freqBar": 26.23604333977085,
        "frontendQuestionId": "207",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Course Schedule",
        "titleSlug": "course-schedule",
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
            "name": "Graph",
            "id": "VG9waWNUYWdOb2RlOjI0",
            "slug": "graph"
          },
          {
            "name": "Topological Sort",
            "id": "VG9waWNUYWdOb2RlOjI2",
            "slug": "topological-sort"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 64.95780492204189,
        "difficulty": "Medium",
        "freqBar": 25.73155663436476,
        "frontendQuestionId": "24",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Swap Nodes in Pairs",
        "titleSlug": "swap-nodes-in-pairs",
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
        "acRate": 47.074493226911876,
        "difficulty": "Medium",
        "freqBar": 24.92110499126798,
        "frontendQuestionId": "139",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Word Break",
        "titleSlug": "word-break",
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
            "name": "Dynamic Programming",
            "id": "VG9waWNUYWdOb2RlOjEz",
            "slug": "dynamic-programming"
          },
          {
            "name": "Trie",
            "id": "VG9waWNUYWdOb2RlOjI3",
            "slug": "trie"
          },
          {
            "name": "Memoization",
            "id": "VG9waWNUYWdOb2RlOjMz",
            "slug": "memoization"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 43.650890288272514,
        "difficulty": "Hard",
        "freqBar": 24.77224362960954,
        "frontendQuestionId": "135",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Candy",
        "titleSlug": "candy",
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
        "acRate": 55.83839054096277,
        "difficulty": "Medium",
        "freqBar": 24.420192765179095,
        "frontendQuestionId": "11",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Container With Most Water",
        "titleSlug": "container-with-most-water",
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
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 57.14354540482825,
        "difficulty": "Medium",
        "freqBar": 24.089796259615245,
        "frontendQuestionId": "138",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Copy List with Random Pointer",
        "titleSlug": "copy-list-with-random-pointer",
        "topicTags": [
          {
            "name": "Hash Table",
            "id": "VG9waWNUYWdOb2RlOjY=",
            "slug": "hash-table"
          },
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
        "acRate": 57.05176910408798,
        "difficulty": "Medium",
        "freqBar": 23.729106034770822,
        "frontendQuestionId": "72",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Edit Distance",
        "titleSlug": "edit-distance",
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
        "acRate": 66.22055568635183,
        "difficulty": "Medium",
        "freqBar": 23.052336527429492,
        "frontendQuestionId": "739",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Daily Temperatures",
        "titleSlug": "daily-temperatures",
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
            "name": "Monotonic Stack",
            "id": "VG9waWNUYWdOb2RlOjYxMDU0",
            "slug": "monotonic-stack"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 57.82082652016892,
        "difficulty": "Medium",
        "freqBar": 23.00124068248778,
        "frontendQuestionId": "90",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Subsets II",
        "titleSlug": "subsets-ii",
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
        "acRate": 45.14043621825496,
        "difficulty": "Hard",
        "freqBar": 22.60780068062119,
        "frontendQuestionId": "84",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Largest Rectangle in Histogram",
        "titleSlug": "largest-rectangle-in-histogram",
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
            "name": "Monotonic Stack",
            "id": "VG9waWNUYWdOb2RlOjYxMDU0",
            "slug": "monotonic-stack"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 66.97093328881414,
        "difficulty": "Medium",
        "freqBar": 22.221258180037243,
        "frontendQuestionId": "215",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Kth Largest Element in an Array",
        "titleSlug": "kth-largest-element-in-an-array",
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
            "name": "Sorting",
            "id": "VG9waWNUYWdOb2RlOjYxMDQ5",
            "slug": "sorting"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          },
          {
            "name": "Quickselect",
            "id": "VG9waWNUYWdOb2RlOjYxMDY5",
            "slug": "quickselect"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 64.58730299692398,
        "difficulty": "Medium",
        "freqBar": 21.64240111587461,
        "frontendQuestionId": "64",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Minimum Path Sum",
        "titleSlug": "minimum-path-sum",
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
            "name": "Matrix",
            "id": "VG9waWNUYWdOb2RlOjYxMDUz",
            "slug": "matrix"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 60.05159597046025,
        "difficulty": "Medium",
        "freqBar": 21.323461192792752,
        "frontendQuestionId": "200",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Number of Islands",
        "titleSlug": "number-of-islands",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 63.345493263861954,
        "difficulty": "Medium",
        "freqBar": 20.34737885389395,
        "frontendQuestionId": "236",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Lowest Common Ancestor of a Binary Tree",
        "titleSlug": "lowest-common-ancestor-of-a-binary-tree",
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
        "acRate": 46.00826328661061,
        "difficulty": "Medium",
        "freqBar": 18.887373032792052,
        "frontendQuestionId": "162",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Find Peak Element",
        "titleSlug": "find-peak-element",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 50.59021781804366,
        "difficulty": "Medium",
        "freqBar": 18.781269791801652,
        "frontendQuestionId": "54",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Spiral Matrix",
        "titleSlug": "spiral-matrix",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
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
        "acRate": 41.247376255789376,
        "difficulty": "Medium",
        "freqBar": 17.71975225658874,
        "frontendQuestionId": "33",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Search in Rotated Sorted Array",
        "titleSlug": "search-in-rotated-sorted-array",
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
        "acRate": 66.54106366962306,
        "difficulty": "Medium",
        "freqBar": 13.64888812825411,
        "frontendQuestionId": "238",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Product of Array Except Self",
        "titleSlug": "product-of-array-except-self",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 40.832050295419585,
        "difficulty": "Easy",
        "freqBar": 10.913339279678416,
        "frontendQuestionId": "20",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Valid Parentheses",
        "titleSlug": "valid-parentheses",
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
        "hasSolution": true,
        "hasVideoSolution": true
      },
      {
        "acRate": 53.319650927656845,
        "difficulty": "Easy",
        "freqBar": 8.386171847133669,
        "frontendQuestionId": "1",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Two Sum",
        "titleSlug": "two-sum",
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
        "hasVideoSolution": true
      },
      {
        "acRate": 58.16185075941769,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "967",
        "isFavor": false,
        "paidOnly": false,
        "status": "ac",
        "title": "Numbers With Same Consecutive Differences",
        "titleSlug": "numbers-with-same-consecutive-differences",
        "topicTags": [
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
        "acRate": 58.301703315662344,
        "difficulty": "Hard",
        "freqBar": 0,
        "frontendQuestionId": "982",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Triples with Bitwise AND Equal To Zero",
        "titleSlug": "triples-with-bitwise-and-equal-to-zero",
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
            "name": "Bit Manipulation",
            "id": "VG9waWNUYWdOb2RlOjE5",
            "slug": "bit-manipulation"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 53.52891318512388,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "1423",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Maximum Points You Can Obtain from Cards",
        "titleSlug": "maximum-points-you-can-obtain-from-cards",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
          },
          {
            "name": "Sliding Window",
            "id": "VG9waWNUYWdOb2RlOjU1ODIx",
            "slug": "sliding-window"
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
        "acRate": 36.58788934872577,
        "difficulty": "Hard",
        "freqBar": 0,
        "frontendQuestionId": "1912",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Design Movie Rental System",
        "titleSlug": "design-movie-rental-system",
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
            "name": "Design",
            "id": "VG9waWNUYWdOb2RlOjI1",
            "slug": "design"
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
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 33.66750208855472,
        "difficulty": "Hard",
        "freqBar": 0,
        "frontendQuestionId": "2019",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "The Score of Students Solving Math Expression",
        "titleSlug": "the-score-of-students-solving-math-expression",
        "topicTags": [
          {
            "name": "Array",
            "id": "VG9waWNUYWdOb2RlOjU=",
            "slug": "array"
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
            "name": "Memoization",
            "id": "VG9waWNUYWdOb2RlOjMz",
            "slug": "memoization"
          }
        ],
        "hasSolution": false,
        "hasVideoSolution": false
      },
      {
        "acRate": 59.80558930741191,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "2093",
        "isFavor": false,
        "paidOnly": true,
        "status": "ac",
        "title": "Minimum Cost to Reach City With Discounts",
        "titleSlug": "minimum-cost-to-reach-city-with-discounts",
        "topicTags": [
          {
            "name": "Graph",
            "id": "VG9waWNUYWdOb2RlOjI0",
            "slug": "graph"
          },
          {
            "name": "Heap (Priority Queue)",
            "id": "VG9waWNUYWdOb2RlOjYxMDUw",
            "slug": "heap-priority-queue"
          },
          {
            "name": "Shortest Path",
            "id": "VG9waWNUYWdOb2RlOjYxMDc2",
            "slug": "shortest-path"
          }
        ],
        "hasSolution": true,
        "hasVideoSolution": false
      },
      {
        "acRate": 56.50874815179891,
        "difficulty": "Medium",
        "freqBar": 0,
        "frontendQuestionId": "2952",
        "isFavor": false,
        "paidOnly": false,
        "status": null,
        "title": "Minimum Number of Coins to be Added",
        "titleSlug": "minimum-number-of-coins-to-be-added",
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
        "hasSolution": false,
        "hasVideoSolution": false
      }
    ]
  }
};

const company = "Flipkart";
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