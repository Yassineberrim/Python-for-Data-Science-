"""Module containing utility functions for ft_package."""


def count_in_list(lst, value):
    """Count occurrences of a value in a list.

    Takes a list and a value, and returns how many times that value
    appears in the list.
    """
    return lst.count(value)
# # 1. Désinstaller l'ancienne version
# python3 -m pip uninstall ft_package -y

# # 2. Nettoyer les anciens fichiers de build
# rm -rf dist build ft_package.egg-info

# # 3. Reconstruire
# python3 -m build

# # 4. Réinstaller
# python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# # 5. Revérifier
# python3 -m pip show -v ft_package
