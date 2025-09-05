# MAT 143 Unit 1 Formula Sheet

## Election Counting Methods

**Majority Rule Decision** — The winner must have more than 50% of the votes to win.

**Plurality** — The candidate with the most votes wins. No majority required.

**Borda Count** — Voting results are organized in a preference table and each ranking is assigned a specific number of points based on how many candidates are in the election. The candidate with the most ranking points is declared the winner.

**Plurality with Elimination** — A series of runoff elections where the candidate with the least amount of first-place votes is removed from the ballot each round. A winner is declared when a candidate has a majority of the first place votes.

**Pairwise Comparison** — Every candidate is compared head to head with other candidates. In each pair of comparisons, the candidate with the greater number of higher rankings is given a point. The candidate with the most points after all head-to head comparisons are made is the winner. The number of pairwise match-ups is n(n-1)/2.

## Apportionment

**Standard Divisor (SD)** — The average number of members of the population that will account for one apportioned item.
SD = total population in a group / total number of items to be apportioned
*Round the standard divisor to 4 decimal places*

**Standard Quota (SQ)** — represents the number of items that will be apportioned to each subgroup
SQ = population of the subgroup / Standard divisor

### Hamilton Method of Apportionment
1. Calculate the standard divisor
2. Calculate the standard quota for each subgroup
3. Calculate the lower quota for each subgroup (Round down)
4. Assign each subgroup the number of resources based on its lower quota
5. Assign any remaining resources based on the fractional remainder of the standard quota, in order from largest to smallest

### Jefferson Method of Apportionment
1. Calculate the Standard divisor
2. Calculate the standard quota for each subgroup
3. Calculate the lower quota (round down)
4. Assign each subgroup the number of resources based on its lower quota
5. If there are remaining resources to be distributed, chose a modified divisor by trial and error until the sum of the lower quotas equals the number of resources to be apportioned

### Webster's Method
1. Calculate the standard divisor
2. Calculate the standard quota for each subgroup. Round each quota to the nearest integer
3. Assign each subgroup the number of resources based on the rounded quota (Round like normal)
4. If there are remaining resources to be distributed, chose a modified divisor by trial and error until the sum of the rounded quotas equals the number of resources to be apportioned
