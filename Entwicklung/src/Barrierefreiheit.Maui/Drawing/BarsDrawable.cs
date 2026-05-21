using Microsoft.Maui.Graphics;

namespace Barrierefreiheit.Maui.Drawing;

public class BarsDrawable : IDrawable
{
    public bool Greyscale { get; set; }

    public void Draw(ICanvas canvas, RectF dirtyRect)
    {
        var fill = Greyscale ? Color.FromArgb("#888888") : Color.FromArgb("#C8102E");
        canvas.FillColor = fill;

        // Werte: 30, 50, 60, 40, 45 (T€)
        canvas.FillRectangle(10,  50, 20, 30);
        canvas.FillRectangle(40,  30, 20, 50);
        canvas.FillRectangle(70,  20, 20, 60);
        canvas.FillRectangle(100, 40, 20, 40);
        canvas.FillRectangle(130, 35, 20, 45);
    }
}
