#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		if (fast == slow)
			return (1);
		slow = slow->next;
	}
	return (0);

}
