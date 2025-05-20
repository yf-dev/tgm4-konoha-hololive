# TGM4 MOD - KONOHA Hololive

This is a mod for TGM4 that replaces all the characters in KONOHA game mode with Hololive characters.

![Screenshot](screenshot.png)

[Watch Play Demo Video](https://www.youtube.com/watch?v=IkiuKzF6EOM)

> [!WARNING]  
> This project is not an official project of Hololive Production.
>
> All rights to each artwork belong to their respective owners and licensees.
> 
> Please check the [Derivative Works Guidelines](https://hololivepro.com/en/terms/) for more information.

## Installation

To install this mod, you need to know how to use the [TGM4 MOD](https://github.com/rishubil/tgm4-mod).

1. Download `tgm4-konoha-hololive.zip` from the [releases page](https://github.com/yf-dev/tgm4-konoha-hololive/releases)
2. Unpack the game files using the TGM4 MOD
3. Remove the `resources/extracted_textures` directory
4. Copy `extracted_textures` from `tgm4-konoha-hololive.zip` into the `resources/extracted_textures` directory
5. Repack the game files using the TGM4 MOD
6. Copy `resources/packed_gamefiles` to your TGM4 installation directory

## Change the characters' order

To change the characters' order, you need to edit the `generate.py` file.

The variable `character_id_list` in this file contains the list of character IDs that you want to use as replacements.
You can change the order of the characters by rearranging the order of the IDs in this list.

After making your changes, run the `generate.py` file to regenerate the `extracted_textures` directory with the new character order.

## Add new characters

To add new characters:

1. Create a new character folder in the `characters` directory (refer to existing folders as examples).
2. Add two required image files to the folder: `egm.png` (character portrait) and `thumb.png` (thumbnail).
3. Register the new character's information in the `characters.py` file.
4. Add the character's ID to the `character_id_list` in the `generate.py` file.
5. Run the `generate.py` file to regenerate the `extracted_textures` directory with the new character.

**Important**: The game supports exactly 50 characters total. Ensure that the length of `character_id_list` does not exceed 50.

## License

MIT License

Please also check the [Derivative Works Guidelines](https://hololivepro.com/en/terms/)
