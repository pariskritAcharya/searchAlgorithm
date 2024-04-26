# searchAlgorithm
This is a search algorithm which divides array into half to find elements.


### Algorithm for searching.
1. list is entered 
2. list is sorted and passed into algorithm
3. get search item from user 
4. list is broken into half of the length so that we can check if half has our search item.
4.1. if half is not our search item it must be less than it or more than it by comparing it we eliminate half of the check list.
5. when list contains only 1 item loop gets ended if the final item is equal to search the search item is founded else it is not in the list.

## Advantage of this algorithm:
- For searching large lists we do not have to search through all the list. Imagine eterating throughout the list when your item is just at the end of list of 1000 items. you could get it sooner if you had started list from the last.
