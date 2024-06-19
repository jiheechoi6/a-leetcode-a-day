class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        zipped = zip(timestamp, username, website)
        # sort the visits
        sortedVisit = sorted(zipped, key = lambda x: x[0])

        # divide by users
        userVisits = defaultdict(list)
        for _, user, site in sortedVisit:
            userVisits[user].append(site)
        
        combsCount = Counter()
        for _, sites in userVisits.items():
            combsCount.update(Counter(set(combinations(sites, 3))))

        return max(sorted(combsCount), key = combsCount.get)
        
