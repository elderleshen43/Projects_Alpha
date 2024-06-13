/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:11:26 by krybalch          #+#    #+#             */
/*   Updated: 2023/01/22 18:11:27 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include "libft.h"

static int	word_count(const char *str, char c)
{
	int		i;
	int		y;

	i = 0;
	y = 0;
	while (*str)
	{
		if (*str != c && y == 0)
		{
			y = 1;
			i++;
		}
		else if (*str == c)
			y = 0;
		str++;
	}
	return (i);
}

static char	*nextwd(const char *str, int start, int end)
{
	char	*wd;
	int		i;

	i = 0;
	wd = malloc((end - start + 1) * sizeof(char));
	while (start < end)
		wd[i++] = str[start++];
	wd[i] = '\0';
	return (wd);
}

char	**ft_split(char const *s, char c)
{
	size_t		i;
	size_t		j;
	int			index;
	char		**split;

	split = malloc((word_count(s, c) + 1) * sizeof(char *));
	if (!s || !split)
		return (NULL);
	i = 0;
	j = 0;
	index = -1;
	while (i <= ft_strlen(s))
	{
		if (s[i] != c && index < 0)
			index = i;
		else if ((s[i] == c || i == ft_strlen(s)) && index >= 0)
		{	
			split[j++] = nextwd(s, index, i);
			index = -1;
		}
		i++;
	}
	split[j] = 0;
	return (split);
}
/*
int	main ()
{
	printf("%s", ft_split("hello.dsfs.dsfs.s", '.')[1]);	
}
*/