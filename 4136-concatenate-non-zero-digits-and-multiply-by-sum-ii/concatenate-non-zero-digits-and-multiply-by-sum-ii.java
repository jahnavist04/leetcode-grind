class Solution {
    static final int MOD = 1_000_000_007;

    public int[] sumAndMultiply(String s, int[][] queries) {
        int n = s.length();

        ArrayList<Integer> pos = new ArrayList<>();
        ArrayList<Integer> digit = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int d = s.charAt(i) - '0';
            if (d != 0) {
                pos.add(i);
                digit.add(d);
            }
        }

        int m = pos.size();

        long[] preSum = new long[m + 1];
        long[] preNum = new long[m + 1];
        long[] pow10 = new long[m + 1];
        pow10[0] = 1;

        for (int i = 1; i <= m; i++)
            pow10[i] = (pow10[i - 1] * 10) % MOD;

        for (int i = 0; i < m; i++) {
            preSum[i + 1] = preSum[i] + digit.get(i);
            preNum[i + 1] = (preNum[i] * 10 + digit.get(i)) % MOD;
        }

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0], r = queries[i][1];

            int left = lowerBound(pos, l);
            int right = upperBound(pos, r) - 1;

            if (left > right) {
                ans[i] = 0;
                continue;
            }

            long sum = preSum[right + 1] - preSum[left];

            int len = right - left + 1;
            long x = (preNum[right + 1]
                    - preNum[left] * pow10[len] % MOD + MOD) % MOD;

            ans[i] = (int) (x * (sum % MOD) % MOD);
        }

        return ans;
    }

    private int lowerBound(ArrayList<Integer> a, int x) {
        int l = 0, r = a.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (a.get(mid) >= x) r = mid;
            else l = mid + 1;
        }
        return l;
    }

    private int upperBound(ArrayList<Integer> a, int x) {
        int l = 0, r = a.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (a.get(mid) > x) r = mid;
            else l = mid + 1;
        }
        return l;
    }
}