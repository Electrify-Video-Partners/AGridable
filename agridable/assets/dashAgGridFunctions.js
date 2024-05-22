var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


function scaleNumber(number, scale) {
    // Define scale factors and their corresponding labels
    const scales = {
        null: { factor: 1, label: '' },
        'thousands': { factor: 1e3, label: 'k' },
        'millions': { factor: 1e6, label: 'm' },
        'billions': { factor: 1e9, label: 'b' },
        'trillions': { factor: 1e12, label: 't' }
    };
    // Get the scale factor and label; default to null if undefined scale is provided
    const scaleInfo = scales[scale] || scales[null];
    const scaleFactor = scaleInfo.factor;
    const scaleLabel = scaleInfo.label;
    // Adjust the number according to the selected scale
    const scaledNumber = number / scaleFactor;
    return [scaledNumber, scaleLabel]
}

function createNumberPrecisionOptions(precision, precision_type) {
    let options = {}
    if (precision_type === 'f') {
        options.minimumFractionDigits = precision
        options.maximumFractionDigits = precision
    } else if (precision_type === 'r') {
        options.minimumSignificantDigits = precision
        options.maximumSignificantDigits = precision
    }
    return options
}

dagfuncs.formatNumber = function (
    number, scale = null, precision = 2, precision_type = 'f', locale = 'en-US'
) {
    // Return null if number is null
    if (number === null) {
        return null;
    }
    // Get scaled number and label
    const [scaledNumber, scaleLabel] = scaleNumber(number, scale)
    // Set number precision
    options = createNumberPrecisionOptions(precision, precision_type)
    // Create the formatter with specified options
    const formatter = new Intl.NumberFormat(locale, options);
    // Format the number and append the scale label
    return formatter.format(scaledNumber) + scaleLabel;
}

dagfuncs.formatPercentage = function (
    number, precision = 2, precision_type = 'f', is_decimal = true, locale = 'en-US'
) {
    // Return null if number is null
    if (number === null) {
        return null;
    }
    if (is_decimal == false) {
        number = number / 100
    }
    // Set number precision
    options = createNumberPrecisionOptions(precision, precision_type)
    // Set percent option
    options.style = 'percent'
    // Create the formatter with specified options
    const formatter = new Intl.NumberFormat(locale, options);
    // Format the number and append the scale label
    return formatter.format(number);
}

dagfuncs.formatCurrency = function (
    number, currencyCode = 'USD', scale = null, precision = 2,
    precision_type = 'f', currencyDisplay = 'symbol', locale = 'en-US'
) {
    // Return null if number is null
    if (number === null) {
        return null;
    }
    // Get scaled number and label
    const [scaledNumber, scaleLabel] = scaleNumber(number, scale)
    // Set number precision
    options = createNumberPrecisionOptions(precision, precision_type)
    // Set currency options
    options.style = 'currency'
    options.currency = currencyCode
    options.currencyDisplay = currencyDisplay
    // Create the formatter with specified options
    const formatter = new Intl.NumberFormat(locale, options);
    // Format the number and append the scale label
    return formatter.format(scaledNumber) + scaleLabel;
}

dagfuncs.formatNumberPrefixSuffix = function (
    number, prefix = null, suffix = null, scale = null, precision = 2,
    precision_type = 'f', locale = 'en-US'
) {
    // Return null if number is null
    if (number === null) {
        return null;
    }
    number = dagfuncs.formatNumber(
        number, scale, precision,
        precision_type, locale
    )
    return `${prefix ? prefix : ''}${number}${suffix ? suffix : ''}`;
}

dagfuncs.formatDuration = function (value, unit, output_unit) {
    if (value === null) {
        return null;
    }
    else if (value < 0) {
        sign = '-';
        value = value / -1;
    } else {
        sign = '';
    }
    let totalSeconds;
    // Convert the input value to total seconds based on the unit
    switch (unit) {
        case 'hours':
            totalSeconds = Math.round(value * 3600);
            break;
        case 'minutes':
            totalSeconds = Math.round(value * 60);
            break;
        case 'seconds':
            totalSeconds = Math.round(value);
            break;
        default:
            throw new Error("Invalid unit. Use 'seconds', 'minutes', or 'hours'.");
    }
    // Calculate hours, minutes, and seconds from total seconds
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    // Pad the hours, minutes, and seconds with zeros if needed
    const paddedHours = hours.toString().padStart(2, '0');
    const paddedMinutes = minutes.toString().padStart(2, '0');
    const paddedSeconds = seconds.toString().padStart(2, '0');
    if (output_unit === 'hours') {
        return `${sign}${paddedHours}:${paddedMinutes}:${paddedSeconds}`;
    } else if (output_unit === 'minutes') {
        return `${sign}${paddedMinutes}:${paddedSeconds}`;
    } else {
        throw new Error("Invalid output_unit. Use 'minutes' or 'hours'")
    }
}

dagfuncs.conditionalFormat = function () {
    for (let i = 0; i < arguments.length; i = i + 3) {
        condition_col_value = arguments[i]
        condition_value = arguments[i + 1]
        formatted_value = arguments[i + 2]
        if (condition_col_value == condition_value) {
            return formatted_value
        }
    }
}