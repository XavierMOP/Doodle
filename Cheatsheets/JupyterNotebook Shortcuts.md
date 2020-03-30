# Command mode vs. Edit mode

Jupyter Notebooks have two different keyboard input modes:

1. **Command mode** - binds the keyboard to notebook level actions. Indicated by a grey cell border with a blue left margin.

2. **Edit mode** - when you’re typing in a cell. Indicated by a green cell border

## Command Mode

- `shift` + `enter` run cell, select below
- `ctrl` + `enter` run cell
- `option` + `enter` run cell, insert below
- `A` insert cell above
- `B` insert cell below
- `C` copy cell
- `V` paste cell
- `D` , `D` delete selected cell
- `shift` + `M` merge selected cells, or current cell with cell below if only one cell selected
- `I` , `I` interrupt kernel
- `0` , `0` restart kernel (with dialog)
- `Y` change cell to `code` mode
- `M` change cell to `markdown` mode
- `Z` undo delete cells
- `Esc` change to command mode

## Edit Mode
- `cmd` + `click` for multi-cursor editing
- `option` + `scrolling click` for column editing
- `cmd` + `/` toggle comment lines
- `tab` code completion or indent
- `shift` + `tab` tooltip
- `ctrl` + `shift` + `-` split cell
