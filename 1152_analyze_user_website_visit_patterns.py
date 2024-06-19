class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        sortedVisits = sorted(zip(timestamp, username, website), key=lambda x: x[0])
        
        userVisits = defaultdict(list)
        for _, user, site in sortedVisits:
            userVisits[user].append(site)

        combCnt = Counter()
        for user, sites in userVisits.items():
            combCnt.update(set(combinations(sites, 3)))

        return max(sorted(combCnt), key=combCnt.get)
        
