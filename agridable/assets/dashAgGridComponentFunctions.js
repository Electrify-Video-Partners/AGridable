var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.formatUrl = function (props) {
    return React.createElement(
        'a',
        { href: props.value },
        'URL'
    );
};

dagcomponentfuncs.formatImg = function (props) {
    const { setData, data } = props;

    function onClick() {
        setData(props.value);
    }

    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
            },
        },
        React.createElement(
            'img',
            {
                onClick,
                style: { width: '100%', height: 'auto' },
                src: props.value,

            },
        )
    );
};