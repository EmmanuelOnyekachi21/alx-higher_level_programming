#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: List instance.
 * Return: 0 if no cycle else 1;
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
