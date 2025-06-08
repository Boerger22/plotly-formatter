import plotly.graph_objects as go

class PlotlyFormatter():
    """
    Unifies the visual style of Plotly figures by applying consistent fonts, layout parameters, and grid settings.

    Attributes can be customized via keyword arguments, otherwise defaults are used. Font sizes for subtitles, axis titles, ticks, and legends are derived from the title font using specified scaling ratios.
    """
    def __init__(self, **kwargs):
        """
        Initialize the PlotlyFormatter with optional style overrides.

        Parameters
        ----------
        title_font : dict, optional
            Font dictionary for the main title (default: {'size': 24, 'family': 'Arial', 'color': 'black'}).
        subtitle_font : dict, optional
            Base font dictionary for subtitle/annotations (size computed from `subtitle_ratio`).
        subtitle_ratio : float, optional
            Ratio of subtitle font size relative to the title font size (default: 0.95).
        axis_title_font : dict, optional
            Base font dictionary for axis titles (size computed from `axis_title_ratio`).
        axis_title_ratio : float, optional
            Ratio of axis title font size relative to the title font (default: 0.9).
        tick_font : dict, optional
            Base font dictionary for axis ticks (size computed from `tick_font_ratio`).
        tick_font_ratio : float, optional
            Ratio of tick font size relative to axis title font (default: 0.9).
        legend_font : dict, optional
            Base font dictionary for legend text (size computed from `legend_font_ratio`).
        legend_font_ratio : float, optional
            Ratio of legend font size relative to title font (default: 0.9).
        showgrid : bool, optional
            Whether to show grid lines (default: True).
        gridcolor : str, optional
            Color of grid lines (default: 'LightGray').
        gridwidth : int, optional
            Width of grid lines (default: 1).
        template : str, optional
            Plotly template to use for figure styling (default: 'simple_white').
        title_x : float, optional
            Horizontal alignment of the figure title (default: 0.5).
        width : int, optional
            Width of the figure in pixels (default: 3200).
        height : int, optional
            Height of the figure in pixels (default: 800).
        """
        defaults = {
            "title_font": {"size":24, "family":"Arial", "color":"black"},
            "subtitle_font": {"family":"Arial", "color":"black"},
            "subtitle_ratio": 0.95,
            "axis_title_font": {"family":"Arial", "color":"black"},
            "axis_title_ratio": 0.9,
            "tick_font": {"family":"Arial", "color":"black"},
            "tick_font_ratio": 0.9,
            "legend_font": {"family":"Arial", "color":"black"},
            "legend_font_ratio": 0.9,
            "showgrid": True,
            "gridcolor": "LightGray",
            "gridwidth": 1,
            "template": "simple_white",
            "title_x": 0.5,
            "width":3200,
            "height":800,
        }

        for key, value in defaults.items():
            setattr(self, key, kwargs.get(key, value))

        self.subtitle_font["size"] = int(self.title_font["size"] * self.subtitle_ratio)
        self.axis_title_font["size"] = int(self.title_font["size"] * self.axis_title_ratio)
        self.tick_font["size"] = int(self.axis_title_font["size"] * self.tick_font_ratio)
        self.legend_font["size"] = int(self.title_font["size"] * self.legend_font_ratio)

    def standardize(self, fig: go.Figure):
        """
        Apply standardized styling to a Plotly figure.

        This method updates axis fonts, layout properties, grid appearance,
        and annotation fonts to ensure a consistent and professional visual style.

        Parameters
        ----------
        fig : plotly.graph_objects.Figure
            The Plotly figure to apply standard styling to. The figure is modified in place.

        Notes
        -----
        - Y-axis and X-axis titles and tick fonts are set using computed sizes.
        - Grid appearance is set according to the configured color and width.
        - Layout-level properties such as title font, legend font, template, height, and width are applied.
        - Any existing annotations in the layout are updated with the subtitle font settings.
        """
        # Update y-axis styling
        fig.update_yaxes(
            title_font=self.axis_title_font,
            tickfont=self.tick_font,
            showgrid=self.showgrid,
            gridcolor=self.gridcolor,
            gridwidth=self.gridwidth,
        )

        # Update x-axis styling
        fig.update_xaxes(
            title_font=self.axis_title_font,
            tickfont=self.tick_font,
            showgrid=self.showgrid,
            gridcolor=self.gridcolor,
            gridwidth=self.gridwidth,
        )

        # Update figure layout (title, legend, template, size, etc.)
        fig.update_layout(
            title_font=self.title_font,
            # title_x=self.title_x,
            legend_font=self.legend_font,
            template=self.template,
            height=self.height,
            width=self.width,
        )

        # Update annotation fonts (treated as subtitles)
        if "annotations" in fig["layout"]:
            for annotation in fig['layout']['annotations']:
                annotation['font'] = self.subtitle_font