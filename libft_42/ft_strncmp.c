/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:06:54 by krybalch          #+#    #+#             */
/*   Updated: 2023/01/22 18:06:55 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	compare_char(char w1, char w2)
{
	if ((unsigned char)w1 != (unsigned char)w2)
		return ((unsigned char)w1 - (unsigned char)w2);
	return (0);
}

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	i = 0;
	while (s1[i] && s2[i] && i < n)
	{
		if (compare_char(s1[i], s2[i]))
			return (compare_char(s1[i], s2[i]));
		i++;
	}
	if (i < n)
		return (compare_char(s1[i], s2[i]));
	return (0);
}

/*int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;
	i = 0;
	while (i < n && s1[i] != '\0' && s2[i] != '\0' && s1[i] == s2[i])
	{
		i++;
	}
	if (i == n)
	{
		return (0);
	}
	return (unsigned char)s1[i] - (unsigned char)s2[i];
}
*/