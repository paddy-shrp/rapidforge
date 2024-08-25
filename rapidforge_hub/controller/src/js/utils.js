function calculateAverage(values) {
    if (values.length == 0) return 0;

    var sum = 0;
    for (let i = 0; i < values.length; i++) sum += values[i];
    return sum / values.length;
}