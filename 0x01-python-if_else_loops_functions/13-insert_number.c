#include "lists.h"

/**
 *insert_node -function that inserts a number into a sorted singly linked list
 *
 * @head: pointer to head
 * @number: number to insert
 *
 * Return:the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;

		while (current_node != NULL && current_node->next->n < number)
	{
		current_node = current_node->next;
	}

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
