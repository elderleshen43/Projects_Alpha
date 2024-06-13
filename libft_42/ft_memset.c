/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:05:20 by krybalch          #+#    #+#             */
/*   Updated: 2023/01/22 18:05:20 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdio.h>
#include <string.h>

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned long	i;

	i = 0;
	while (n > i)
	{
		((unsigned char *)s)[i] = c;
		i++;
	}
	return (s);
}

/*
int	main(void)
{
	int	i = 8;
	char	c = "c";
	
	char	str[] = "This is a test string"
	printf("Printing test str [%s]\n", str);
	printf("Set char [%c] %dx to str \n", c, i);
	ft_memset(str, c, i);
	printf("Printing after memset [%s]", str);
	return (0);
}
*/