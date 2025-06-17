const formatCurrencyToBRL = (value) => {
    const normalizedData = value.replace(/\./g, '').replace(',', '.');

    return Number(normalizedData).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
};

const formatDateToDMY = (date) => {
    return dayjs(date).format('DD/MM/YYYY');
};
