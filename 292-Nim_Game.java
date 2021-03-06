/**
 * 292. Nim Game
 * https://leetcode.com/problems/nim-game/
 *
 * You are playing the following Nim Game with your friend: 
 * There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
 * The one who removes the last stone will be the winner. 
 * You will take the first turn to remove the stones.
 *
 * Both of you are very clever and have optimal strategies for the game. 
 * Write a function to determine whether you can win the game given the number of stones in the heap.
 * 
 * For example, if there are 4 stones in the heap, then you will never win the game: 
 * no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
 *
 */ 
public class Solution {

    /**
     * Given a player must take 1, 2, or 3 stones
     * and the winner must take the last stone
     * 
     * TLDR; If the number of stones is divisible by 4, given perfect play, the first player will lose
     *
     * Looking at a table of the first couple plays that could be made and if first player can win...
     * Number Remaining -> Can Win? (Note: Perfect Play)
     * 1 -> True 
     * 2 -> True
     * 3 -> True
     * 4 -> False
     * 
     * The first three are obvious, given we could simply take all the stones 
     * and when considering perfect play, once we introduce the 4th, it's still quite easy to see that
     * no matter how many we take, it''ll always leave at least 1 behind for the opponent to win.
     * 
     * What if this were extended further?
     * Number Remaining -> Can Win? (Note: Perfect Play)
     * 1 -> True 
     * 2 -> True
     * 3 -> True
     * 4 -> False
     * 5 -> True 
     * 6 -> True
     * 7 -> True
     * 8 -> False
     * 
     * Ok now why?
     * It was easy to see that when we had 4 we would lose because 
     * we would reach a state that we would always leave at least 1 behind for the opponent.
     * With the same logic, if we were to leave an opponent with 4, they would be in the same situation
     * that we would have been. So for 5, 6, and 7 stones, we can take our 1, 2, or 3 respectively to leave them at just that.
     * 
     * Likewise for 8, the opponent has the ability to leave us in that 4 position where, no matter how many we take,
     * they'll take the leftovers that leave us at 4.
     * 
     * I think it's from here we begin to really see the pattern and understand the solution.
     * That for any number of stones, if its not divisible by 4, the first player is guaranteed to win, 
     * simply by taking a number of stones that would leave the opponent with a number of stones divisible by 4.
     * If it is divisible by 4, the first player will lose, given perfect play, because no matter how many they take,
     * the opposing player will recursively leave them at a number divisible by 4 until finally, 
     * the first player takes any number from the final 4 leaving 1, 2, or 3 for the second play to take and win.
     * 
     */
    public boolean canWinNim(int numberOfStones) {
        return numberOfStones % 4 != 0;
    }
}
