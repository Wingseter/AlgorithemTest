def find_xy(n):
    s_h, e_h = 1, 141
    while s_h <= e_h:
        m_h = (s_h + e_h) // 2
        min_n = (m_h - 1) * m_h // 2 + 1
        max_n = m_h * (m_h + 1) // 2
        if n < min_n:
            e_h = m_h - 1
        elif n > max_n:
            s_h = m_h + 1
        else:
            x = m_h
            y = n - min_n + 1
            break
    return x, y

def find_xy2(start, end):
    start_pos = None
    end_pos = None

    flore = 1
    flore_start_num = 1
    flore_end_num = 1
    while start_pos is None or end_pos is None:
        if flore_start_num <= start <= flore_end_num:
            start_pos = (flore, start - flore_start_num + 1)
        if flore_start_num <= end <= flore_end_num:
            end_pos = (flore, end - flore_start_num + 1)
        flore_start_num += flore 
        flore += 1
        flore_end_num = flore_start_num + flore - 1

    return start_pos, end_pos
print(find_xy(2))
print(find_xy2(1,3))
