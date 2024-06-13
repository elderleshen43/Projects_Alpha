/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:07:23 by krybalch          #+#    #+#             */
/*   Updated: 2023/01/22 18:07:24 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strnstr(const char *s1, const char *s2, size_t len)
{
	size_t	i;
	size_t	j;

	if (s1 == NULL && len == 0)
		return (0);
	if (!*s2 || s1 == s2)
		return ((char *)s1);
	i = 0;
	while (s1[i] && i < len)
	{
		j = 0;
		while (s1[i + j] && s2[j] && (i + j) < len && s1[i + j] == s2[j])
		{
			j++;
		}
		if (!s2[j])
			return ((char *)&s1[i]);
		i++;
	}
	return (0);
}
