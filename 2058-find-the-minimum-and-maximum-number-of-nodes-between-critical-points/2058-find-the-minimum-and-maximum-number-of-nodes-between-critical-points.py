class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = []
        while head:
            a.append(head.val)
            head = head.next

        p = []
        for i in range(1, len(a) - 1):
            if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
                p.append(i)

        if len(p) < 2:
            return [-1, -1]

        mn = min(p[i] - p[i-1] for i in range(1, len(p)))
        mx = p[-1] - p[0]

        return [mn, mx]