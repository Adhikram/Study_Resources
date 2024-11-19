package Questions.SegmentTree;

/*
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
*/

public class RangeModule {
    SegmentNode root; // Root of the segment tree
    int max = (int) Math.pow(10, 9); // Maximum range value

    // Constructor to initialize the RangeModule
    public RangeModule() {
        root = new SegmentNode(0, max, false); // Initialize root with range [0, max) and state false
    }

    // Method to add a range [left, right)
    public void addRange(int left, int right) {
        update(root, left, right, true); // Update the segment tree with the new range
    }

    // Helper method to update the segment tree
    private boolean update(SegmentNode node, int l, int r, boolean state) {
        // If the current node range is completely within the update range
        if (l <= node.l && r >= node.r) {
            node.state = state; // Update the state
            node.left = null; // Remove left child
            node.right = null; // Remove right child
            return node.state;
        }
        // If there is no overlap
        if (l >= node.r || r <= node.l) return node.state;

        // Split the node
        int mid = (node.r + node.l) >> 1;
        if (node.left == null) {
            node.left = new SegmentNode(node.l, mid, node.state); // Create left child
            node.right = new SegmentNode(mid, node.r, node.state); // Create right child
        }
        // Continue the update on left and right children
        boolean left = update(node.left, l, r, state);
        boolean right = update(node.right, l, r, state);
        return node.state = left && right;
    }

    // Method to query if a range [left, right) is completely tracked
    public boolean queryRange(int left, int right) {
        return query(root, left, right); // Query the segment tree
    }

    // Helper method to query the segment tree
    private boolean query(SegmentNode node, int l, int r) {
        // If there is no overlap
        if (l >= node.r || r <= node.l) return false;
        // If the current node range is completely within the query range or if it is a leaf node
        if ((l <= node.l && r >= node.r) || (node.left == null)) return node.state;
        int mid = (node.r + node.l) >> 1;
        // Query the left or right child based on the range
        if (r <= mid) {
            return query(node.left, l, r);
        } else if (l >= mid) {
            return query(node.right, l, r);
        } else {
            return query(node.left, l, r) && query(node.right, l, r);
        }
    }

    // Method to remove a range [left, right)
    public void removeRange(int left, int right) {
        update(root, left, right, false); // Update the segment tree to remove the range
    }

    // Main method for testing
    public static void main(String[] args) {
        RangeModule rangeModule = new RangeModule();
        rangeModule.addRange(10, 20);
        rangeModule.removeRange(14, 16);
        System.out.println(rangeModule.queryRange(10, 14)); // return True,(Every number in [10, 14) is being tracked)
        System.out.println(rangeModule.queryRange(13, 15)); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
        System.out.println(rangeModule.queryRange(16, 17)); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
    }
}

// Class representing a node in the segment tree
class SegmentNode {
    public int l, r; // Range [l, r)
    public boolean state; // State of the range (tracked or not)
    public SegmentNode left, right; // Left and right children

    // Constructor to initialize a segment node
    public SegmentNode(int l, int r, boolean state) {
        this.l = l;
        this.r = r;
        this.state = state;
    }
}